from django.db import models
from django.core.exceptions import ValidationError


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AtomicComponent(TimestampedModel):
    stock_code = models.CharField(max_length=255, null=False)
    part_code = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    warehouse_location = models.IntegerField(blank=True, null=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    availability = models.IntegerField(null=False, default=0)

    def save(self, *args, **kwargs):
        if self.stock_code is "":
            raise ValidationError('stock_code cannot be empty.')
        else:
            super(AtomicComponent, self).save(*args, **kwargs)


class AtomicRequirementModel(TimestampedModel):

    class Meta:
        abstract = True


class BlueprintRequirementModel(TimestampedModel):

    class Meta:
        abstract = True
