from django.db import models
from shop.models import TimestampedModel
from shop.concept.models import Blueprint, AtomicPrerequisite, BlueprintPrerequisite

class AtomicSpecification(TimestampedModel):

    atomic_requirement = models.ForeignKey(AtomicPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                           null=False)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return "AtomicSpecification: {}: {}".format(self.atomic_component.stock_code, self.quantity)


class BlueprintSpecification(TimestampedModel):

    blueprint_requirement = models.ForeignKey(BlueprintPrerequisite, on_delete=models.PROTECT, related_name='build_with',
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

    # def available(self):
    # 	results = []
    # 	for atm_req in self.atomic_requirements.all():
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

    def getLocalAtomicDependencies(self):
        """
        Return local AtomicSpecification only
        :return: list[AtomicSpecification]
        """
        l = []
        for req in self.atomic_specifications.all():
            l.append(req)
        return l

    def listAtomicDependencies(self):
        """
        Return all atomic dependencies recursively
        return list instead of queryset

        :return: list[AtomicSpecification]
        """
        if len(self.blueprint_specifications.all()) == 0:
            # If no further blueprint dependencies
            return self.getLocalAtomicDependencies()
        else:
            atomicReq = self.getLocalAtomicDependencies()
            for bpReq in self.blueprint_requirements.all():
                atomicReq.extend(bpReq.blueprint_component.listAtomicDependencies())
            return atomicReq
