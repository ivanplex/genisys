from rest_framework import serializers
from shop.atomic.models import (
    AtomicComponent,
    AtomicPrerequisite,
    AtomicSpecification,
    AtomicGroup
)
from shop.attribute.models import Attribute
from shop.attribute.serializers import AttributeSerializer


class AtomicComponentSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)
    warehouse_location = serializers.CharField(required=False)
    material = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False)
    attribute = AttributeSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = AtomicComponent
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        if 'attribute' in validated_data:
            attribute_data = validated_data.pop('attribute')
            atomic_component = AtomicComponent.objects.create(**validated_data)
            for attribute in attribute_data:
                attr = Attribute.objects.create(**attribute)
                atomic_component.attribute.add(attr)
            atomic_component.save()
        else:
            atomic_component = AtomicComponent.objects.create(**validated_data)
        return atomic_component


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
