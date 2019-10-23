from django.db import models
from django.core.exceptions import ValidationError
from shop.models import TimestampedModel
from shop.relations.models import Prerequisite, Specification
from shop.attribute.models import Attribute
from shop.group.models import Group
from django.utils.translation import gettext_lazy as _


class AtomicComponent(TimestampedModel):
    stock_code = models.CharField(max_length=255, null=False) # Req
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True) # Req
    cost = models.FloatField(default=0)
    warehouse_location = models.CharField(blank=True, null=True, max_length=255)
    material = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, null=True) # Req
    availability = models.IntegerField(null=False, default=0)
    attribute = models.ManyToManyField(Attribute, related_name='atom_attr')

    def save(self, *args, **kwargs):
        if self.stock_code is "":
            raise ValidationError('stock_code cannot be empty.')
        else:
            super(AtomicComponent, self).save(*args, **kwargs)


class AtomicGroup(Group):
    members = models.ManyToManyField(AtomicComponent, related_name='members')


class AtomicPrerequisite(Prerequisite):
    atomic_component = models.ForeignKey(AtomicComponent, on_delete=models.PROTECT, related_name='requires',
                                         null=True)
    atomic_group = models.ForeignKey(AtomicGroup, on_delete=models.PROTECT, related_name='allowed_group', null=True)

    def save(self, *args, **kwargs):
        if self.atomic_component is None and self.atomic_group is None:
            raise ValidationError(
                _('AtomicPrerequisite has no assigned product or atomic-group'),
                code='invalid',
            )
        super(AtomicPrerequisite, self).save(*args, **kwargs)


class AtomicSpecification(Specification):
    selected_component = models.ForeignKey(AtomicComponent,  on_delete=models.PROTECT, related_name='using',
                                         null=True)
    prerequisite = models.ForeignKey(AtomicPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                      null=False)
