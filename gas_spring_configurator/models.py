from django.db import models


class ConfiguratorStep(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255, null=False, blank=False)
    selected = models.IntegerField(null=True, blank=False, default=None)
    order = models.IntegerField(null=False, blank=False)
    disabled = models.BooleanField(default=False)
