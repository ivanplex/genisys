from rest_framework import serializers
from shop.atomic.models import (
    AtomicComponent,
    AtomicPrerequisite,
    AtomicSpecification,
    AtomicAttribute,
    AtomicGroup
)


class AtomicAttributeSerializer(serializers.ModelSerializer):

    atomic_component = serializers.PrimaryKeyRelatedField(queryset=AtomicComponent.objects.all())

    class Meta:
        model = AtomicAttribute
        fields = (
            '__all__'
        )


class AtomicComponentSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)
    warehouse_location = serializers.CharField(required=False)
    material = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False)
    attribute = AtomicAttributeSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = AtomicComponent
        fields = (
            '__all__'
        )


class AtomicPrerequisiteSerializer(serializers.ModelSerializer):

    atomic_component = serializers.PrimaryKeyRelatedField(queryset=AtomicComponent.objects.all(), required=False)
    atomic_group = serializers.PrimaryKeyRelatedField(queryset=AtomicGroup.objects.all(), required=False)

    class Meta:
        model = AtomicPrerequisite
        fields = (
            '__all__'
        )


class AtomicSpecificationSerializer(serializers.ModelSerializer):

    selected_component = serializers.PrimaryKeyRelatedField(queryset=AtomicComponent.objects.all())
    prerequisite = serializers.PrimaryKeyRelatedField(queryset=AtomicPrerequisite.objects.all())

    class Meta:
        model = AtomicSpecification
        fields = (
            '__all__'
        )
