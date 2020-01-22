from django.db import models
from modular_assembly.models import TimestampedModel, URL, OffsetImageURL


class Group(TimestampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)

    thumbnail_image = models.ForeignKey(URL, on_delete=models.PROTECT, related_name='group_thumbnail_images', null=True)
    illustration_images = models.ManyToManyField(OffsetImageURL, related_name='group_illustration_images',
                                                 symmetrical=False)
    description_images = models.ManyToManyField(URL, related_name='group_description_images', symmetrical=False)
