from django.db import models
from shop.models import TimestampedModel
from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification

class Blueprint(TimestampedModel):
    name = models.CharField(max_length=250)
    atomic_prerequisites = models.ManyToManyField(AtomicPrerequisite, related_name='atomic_requirements', symmetrical=False)
    build_prerequisites = models.ManyToManyField('BuildPrerequisite', related_name='blueprint_requirements',
                                                     symmetrical=False)

    def isEmpty(self):
        if len(self.atomic_prerequisites.all()) == 0 and len(self.build_prerequisites.all()) == 0:
            return True
        else:
            return False

    def getLocalAtomicPrerequisites(self):
        """
        Return local AtomicPrerequisite only
        :return: list[AtomicRequirement]
        """
        l = []
        for prereq in self.atomic_prerequisites.all():
            l.append(prereq)
        return l

    def allAtomicPrerequisites(self):
        """
        Return all atomic prerequisites recursively
        return list instead of queryset

        :return: list[AtomicRequirement]
        """
        if len(self.build_prerequisites.all()) == 0:
            # If no further blueprint dependencies
            return self.getLocalAtomicPrerequisites()
        else:
            atomicReq = self.getLocalAtomicPrerequisites()
            for bpReq in self.build_prerequisites.all():
                atomicReq.extend(bpReq.build.blueprint.allAtomicPrerequisites())
            return atomicReq

    def getLocalBuildPrerequisites(self):
        """
        Return local BuildPrerequisite only
        :return: list[AtomicRequirement]
        """
        l = []
        for prereq in self.build_prerequisites.all():
            l.append(prereq)
        return l

    def allBuildPrerequisites(self):
        """
        Return all build prerequisites recursively
        return list instead of queryset

        :return: list[AtomicRequirement]
        """
        if len(self.build_prerequisites.all()) == 0:
            # If no further blueprint dependencies
            return []
        else:
            buildPrereq = self.getLocalBuildPrerequisites()
            for prereq in self.build_prerequisites.all():
                buildPrereq.extend(prereq.build.blueprint.getLocalBuildPrerequisites())
            return buildPrereq

    def map_prerequisites(self):
        struct = {}
        struct['name'] = self.name
        struct['atomic_prereq'] = self.getLocalAtomicPrerequisites()
        struct['build_prereq'] = []

        for prereq in self.build_prerequisites.all():
            struct['build_prereq'].append(prereq.build.blueprint.map_prerequisites())
        return struct

class BuildPrerequisite(TimestampedModel):
    build = models.ForeignKey('Build', on_delete=models.PROTECT, related_name='requires',
                              null=False)

    min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)


class BuildSpecification(TimestampedModel):
    build_prereq = models.ForeignKey(BuildPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                     null=False)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)


class Build(TimestampedModel):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=3)
    availability = models.IntegerField(null=False, default=0)

    blueprint = models.ForeignKey(Blueprint, on_delete=models.PROTECT, related_name='based_on', null=False)

    atomic_specifications = models.ManyToManyField(AtomicSpecification, related_name='atomic_specification', symmetrical=False)
    build_specifications = models.ManyToManyField(BuildSpecification, related_name='build_specification', symmetrical=False)

    def hasBuildPrerequisite(self):
        return False if not self.blueprint.build_prerequisites.all() else True

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

class PrerequisiteAudit:
    """
    Prerequisite auditing for builds
    """
    deficit = []
    surplus = []

    def fulfilled(self):
        if not self.deficit and not self.surplus:
            return True
        else:
            return False

