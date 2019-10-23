from django.db import models
from shop.models import TimestampedModel


class Attribute(TimestampedModel):
    VISIBILITY_CHOICE = [
        ('online', 'online'),
        ('inherit', 'inherit')
    ]
    key = models.CharField(max_length=255, blank=False, null=False)
    value = models.CharField(max_length=255, blank=False, null=False)
    visibility = models.CharField(max_length=255, blank=True, null=True, choices=VISIBILITY_CHOICE)

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get(self, key):
        return self.objects.filter(key=key)
