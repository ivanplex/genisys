from django.db import models
from shop.models import TimestampedModel, AtomicComponent, AtomicPrerequisiteModel, BlueprintPrerequisiteModel


class AtomicPrerequisite(AtomicPrerequisiteModel):
    atomic_component = models.ForeignKey(AtomicComponent, on_delete=models.PROTECT, related_name='requires',
                                         null=False)
    min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    # def available(self):
    # 	return True if self.quantity <= self.atomic_component.availability else False

    def __str__(self):
        return "AtomicRequirement: {}: {} - {}".format(self.atomic_component.stock_code, self.min_quantity,
                                                       self.max_quantity)


class BlueprintPrerequisite(BlueprintPrerequisiteModel):
    blueprint_component = models.ForeignKey('Blueprint', on_delete=models.PROTECT, related_name='requires',
                                            null=False)

    min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)


class Blueprint(TimestampedModel):
    name = models.CharField(max_length=250)
    atomic_prerequisites = models.ManyToManyField(AtomicPrerequisite, related_name='atomic_requirements', symmetrical=False)
    blueprint_prerequisites = models.ManyToManyField(BlueprintPrerequisite, related_name='blueprint_requirements',
                                                     symmetrical=False)

    def isEmpty(self):
        if len(self.atomic_prerequisites.all()) == 0 and len(self.blueprint_prerequisites.all()) == 0:
            return True
        else:
            return False

    def getLocalAtomicPrerequisites(self):
        """
        Return local AtomicRequirement only
        :return: list[AtomicRequirement]
        """
        l = []
        for req in self.atomic_prerequisites.all():
            l.append(req)
        return l

    def listAtomicDependencies(self):
        """
        Return all atomic dependencies recursively
        return list instead of queryset

        :return: list[AtomicRequirement]
        """
        if len(self.blueprint_prerequisites.all()) == 0:
            # If no further blueprint dependencies
            return self.getLocalAtomicPrerequisites()
        else:
            atomicReq = self.getLocalAtomicPrerequisites()
            for bpReq in self.blueprint_prerequisites.all():
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
