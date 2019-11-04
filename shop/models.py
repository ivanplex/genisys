from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class URL(TimestampedModel):
    url = models.URLField(null=False)


class OffsetImageURL(URL):
    offset_x = models.IntegerField(default=0, null=False, blank=False, help_text="Image offset x direction")
    offset_y = models.IntegerField(default=0, null=False, blank=False, help_text="Image offset y direction")
