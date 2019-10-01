from django.db import models
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from shop.models import TimestampedModel
from shop.atomic.models import AtomicComponent
from shop.assembly.models import Product


class AtomicGroup(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)
    members = models.ManyToManyField(AtomicComponent, related_name='members')


class ProductGroup(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)
    members = models.ManyToManyField(Product, related_name='members')
