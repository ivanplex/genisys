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
            '__all__'
        )


class AtomicPrerequisiteSerializer(serializers.ModelSerializer):

    atomic_component = AtomicComponentSerializer()

    class Meta:
        model = AtomicPrerequisite
        fields = (
            '__all__'
        )