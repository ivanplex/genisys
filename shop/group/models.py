from django.db import models
from shop.models import TimestampedModel


class Group(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)
