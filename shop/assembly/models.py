from django.db import models
from shop.models import TimestampedModel
from shop.concept.models import Blueprint, AtomicPrerequisite, BlueprintPrerequisite, PrerequisiteAudit


class AtomicSpecification(TimestampedModel):
    atomic_prereq = models.ForeignKey(AtomicPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                      null=False)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    def validate(self):
        """
        Valiate quantity following prerequisite constraint
        :return: Bool
        """
        return True if self.atomic_prereq.min_quantity <= self.quantity <= self.atomic_prereq.max_quantity else False

    def __str__(self):
        return "AtomicSpecification: {}: {}".format(self.atomic_prereq.atomic_component.stock_code, self.quantity)


class BlueprintSpecification(TimestampedModel):
    blueprint_prereq = models.ForeignKey(BlueprintPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                         null=False)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return "BlueSpecification: {}: {}".format(self.atomic_component.stock_code, self.quantity)


class Build(TimestampedModel):
    name = models.CharField(max_length=250)
    blueprint = models.ForeignKey(Blueprint, on_delete=models.PROTECT, related_name='based_on', null=False)

    atomic_specifications = models.ManyToManyField(AtomicSpecification, related_name='specifications',
                                                   symmetrical=False)
    blueprint_specifications = models.ManyToManyField(BlueprintSpecification, related_name='specifications',
                                                      symmetrical=False)

    def validate(self):
        """
        Valiate quantity following prerequisite constraint
        :return: Bool
        """
        # TODO: Make this recursive
        for spec in self.atomic_specifications.all():
            if spec.validate():
                continue
            else:
                return False
        return True

    def prerequisiteAudit(self):

        deficit = PrerequisiteAudit()

        deficit.deficit = [x for x in self.blueprint.getLocalAtomicPrerequisites()
                     if x not in self.getLocalAtomicPrerequisites()]
        deficit.surplus = [x for x in self.getLocalAtomicPrerequisites()
                     if x not in self.blueprint.getLocalAtomicPrerequisites()]
        return deficit

    # def available(self):
    # 	results = []
    # 	for atm_req in self.atomic_prerequisites.all():
    # 		results.append(atm_req.available())
    #
    # 	return all(results)

    def available(self):
        for requirement in self.listAtomicDependencies():
            if requirement.atomic_component.availability >= requirement.quantity:
                continue
            else:
                return False
        return True

    def getLocalAtomicSpecifications(self):
        """
        Return local AtomicSpecification only
        :return: list[AtomicSpecification]
        """
        l = []
        for req in self.atomic_specifications.all():
            l.append(req)
        return l

    def getLocalAtomicPrerequisites(self):
        """
        Return a list of AtomicPrerequsites
        specified by all atomicSpecifications
        in the blueprint

        :return: list[AtomicPrerequsites]
        """
        l = []
        for spec in self.atomic_specifications.all():
            l.append(spec.atomic_prereq)
        return l

    def listAtomicDependencies(self):
        """
        Return all atomic dependencies recursively
        return list instead of queryset

        :return: list[AtomicSpecification]
        """
        if len(self.blueprint_specifications.all()) == 0:
            # If no further blueprint dependencies
            return self.getLocalAtomicSpecifications()
        else:
            atomicReq = self.getLocalAtomicSpecifications()
            for bpReq in self.blueprint_specifications.all():
                atomicReq.extend(bpReq.blueprint_component.listAtomicDependencies())
            return atomicReq
