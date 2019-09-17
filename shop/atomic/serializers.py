from rest_framework import serializers
from .models import AtomicComponent


class AtomicComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtomicComponent
        fields = (
            'id',
            'name',
            'stock_code',
        )
