from django.db import models
from shop.models import TimestampedModel
from shop.atomic.models import AtomicComponent, AtomicPrerequisite
from shop.assembly.models import Product, Blueprint


class Group(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)


class AtomicGroup(Group):
    members = models.ManyToManyField(AtomicComponent, related_name='members')


class BlueprintGroup(Group):
    members = models.ManyToManyField(Blueprint, related_name='members')


class ProductGroup(Group):
    members = models.ManyToManyField(Product, related_name='members')
