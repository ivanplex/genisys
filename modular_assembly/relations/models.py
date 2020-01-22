from django.db import models
from modular_assembly.models import TimestampedModel


class Prerequisite(TimestampedModel):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)


class Specification(TimestampedModel):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

