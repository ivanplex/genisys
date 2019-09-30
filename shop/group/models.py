from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from shop.models import TimestampedModel


class Group(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)

    member_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    member_object = GenericForeignKey('content_type', 'object_id')
