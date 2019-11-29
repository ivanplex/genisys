from django.db import models
from django.core.exceptions import ValidationError
from shop.models import TimestampedModel, URL, OffsetImageURL
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
    availability = models.IntegerField(null=False, default=0)
    attribute = models.ManyToManyField(Attribute, related_name='atom_attr')

    thumbnail_image = models.ForeignKey(URL, on_delete=models.PROTECT, related_name='atomic_thumbnail', null=True)
    illustration_images = models.ManyToManyField(OffsetImageURL, related_name='atomic_illustration',
                                               symmetrical=False)
    description_images = models.ManyToManyField(URL, related_name='atomic_description_image', symmetrical=False)

    retail_price = models.FloatField(verbose_name='Retail Price', default=0, null=False)
    retail_price_per_unit = models.FloatField(verbose_name='Retail Price per unit', default=0, null=False)
    retail_unit_measurement = models.CharField(max_length=255, null=True, blank=True)
    internal_cost = models.FloatField(default=0, null=False)

    component_factor = models.FloatField(default=0, null=False, blank=False)

    def save(self, *args, **kwargs):
        if self.stock_code is "":
            raise ValidationError('stock_code cannot be empty.')
        else:
            super(AtomicComponent, self).save(*args, **kwargs)

    def getComponentFactor(self):
        return self.component_factor


class AtomicGroup(Group):
    members = models.ManyToManyField(AtomicComponent, related_name='members')


class AtomicPrerequisite(Prerequisite):
    atomic_component = models.ForeignKey(AtomicComponent, on_delete=models.PROTECT, related_name='requires',
                                         null=True)
    atomic_group = models.ForeignKey(AtomicGroup, on_delete=models.PROTECT, related_name='allowed_group', null=True)
    virtual = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.atomic_component is None and self.atomic_group is None and self.virtual is False:
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
