from rest_framework import serializers
from shop.atomic.models import AtomicComponent, AtomicPrerequisite


class AtomicComponentSerializer(serializers.ModelSerializer):

    part_code = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    warehouse_location = serializers.CharField(required=False)
    material = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False)

    class Meta:
        model = AtomicComponent
        fields = (
            'id',
            'stock_code',
            'part_code',
            'description',
            'warehouse_location',
            'material',
            'weight',
            'image',
            'availability',
        )


class AtomicPrerequisiteSerializer(serializers.ModelSerializer):

    atomic_component = AtomicComponentSerializer()

    class Meta:
        model = AtomicPrerequisite
        fields = (
            'atomic_component',
            'min_quantity',
            'max_quantity'
        )
