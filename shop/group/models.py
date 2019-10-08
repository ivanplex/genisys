from django.db import models
from shop.models import TimestampedModel
from shop.atomic.models import AtomicComponent, AtomicPrerequisite
from shop.assembly.models import Product, Blueprint


class AtomicGroup(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    auto_generated = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    members = models.ManyToManyField(AtomicComponent, related_name='members')


class BlueprintGroup(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)
    members = models.ManyToManyField(Blueprint, related_name='members')


class ProductGroup(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)
    members = models.ManyToManyField(Product, related_name='members')
