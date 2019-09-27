from django.db import models
from shop.models import TimestampedModel
from shop.assembly.models import Blueprint


class KeyValueAttribute(TimestampedModel):
    key = models.CharField(max_length=255, blank=False, null=False)
    value = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        abstract = True

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class BlueprintAttribute(KeyValueAttribute):
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE,
                                  related_name='blueprint_attribute', null=False)


class AtomAttribute(KeyValueAttribute):
    atomic_component = models.ForeignKey(Blueprint, on_delete=models.CASCADE,
                                  related_name='atom_attribute', null=False)
