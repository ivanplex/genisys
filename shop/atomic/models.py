from django.db import models
from django.core.exceptions import ValidationError
from shop.models import TimestampedModel
from shop.attribute.models import KeyValueAttribute


class AtomicAttribute(KeyValueAttribute):
    atomic_component = models.ForeignKey('AtomicComponent', on_delete=models.CASCADE,
                                  related_name='atom_attribute', null=False)


class AtomicComponent(TimestampedModel):
    stock_code = models.CharField(max_length=255, null=False)
    part_code = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    warehouse_location = models.IntegerField(blank=True, null=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    availability = models.IntegerField(null=False, default=0)

    def attribute(self):
        attr = AtomicAttribute.objects.filter(atomic_component=self)
        return attr

    def save(self, *args, **kwargs):
        if self.stock_code is "":
            raise ValidationError('stock_code cannot be empty.')
        else:
            super(AtomicComponent, self).save(*args, **kwargs)


class AtomicPrerequisite(TimestampedModel):
    atomic_component = models.ForeignKey(AtomicComponent, on_delete=models.PROTECT, related_name='requires',
                                         null=False)
    min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    # def available(self):
    # 	return True if self.quantity <= self.atomic_component.availability else False

    def __str__(self):
        return "AtomicRequirement: {}: {} - {}".format(self.atomic_component.stock_code, self.min_quantity,
                                                       self.max_quantity)


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
