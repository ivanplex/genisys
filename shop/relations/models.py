from django.db import models
from shop.models import TimestampedModel


class Prerequisite(TimestampedModel):
    min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)


class Specification(TimestampedModel):
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

