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

    def validate(self):
        """
        Valiate quantity following prerequisite constraint
        :return: Bool
        """
        return True if self.build_prereq.min_quantity <= self.quantity <= self.build_prereq.max_quantity else False


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
        Validate the following
        - Prerequisite compliance
        - Prerequisite quantity constraints
        :return:
        """
        return True if self.validate_spec() and self.prerequisiteAudit().fulfilled() else False

    def validate_spec(self):
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

        # Add blueprint deficit
        blueprint_spec_prereq = [x.build_prereq for x in self.getLocalBuildSpecifications()]
        blueprint_deficit = [x for x in self.blueprint.getLocalBuildPrerequisites()
                     if x not in blueprint_spec_prereq]

        blueprint_surplus = [x for x in blueprint_spec_prereq
                     if x not in self.blueprint.getLocalBuildPrerequisites()]
        deficit.deficit.extend(blueprint_deficit)
        deficit.deficit.extend(blueprint_surplus)

        return deficit


    # def available(self):
    #     for requirement in self.listAtomicDependencies():
    #         if requirement.atomic_component.availability >= requirement.quantity:
    #             continue
    #         else:
    #             return False
    #     return True

    def getLocalAtomicSpecifications(self):
        """
        Return local AtomicSpecification only
        :return: list[AtomicSpecification]
        """
        l = []
        for spec in self.atomic_specifications.all():
            l.append(spec)
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

    def getLocalBuildSpecifications(self):
        """
        Return local BuildSpecification only
        :return: list[AtomicSpecification]
        """
        l = []
        for spec in self.build_specifications.all():
            l.append(spec)
        return l

    def map_spec(self):
        struct = {}
        struct['name'] = self.name
        struct['atomic_spec'] = self.getLocalAtomicSpecifications()
        struct['build_spec'] = []
        struct['audit'] = self.prerequisiteAudit().__str__()

        for spec in self.build_specifications.all():
            struct['build_spec'].append(spec.build_prereq.build.map_spec())
        return struct

#TODO: Redefine how to handle Audits
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

    def __str__(self):
        return "Audit: Deficit-{}: Surplus-{}".format(len(self.deficit), len(self.surplus))

