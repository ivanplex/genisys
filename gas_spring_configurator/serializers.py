from rest_framework import serializers
from .models import ConfiguratorStep
from modular_assembly.assembly.models import (
    Blueprint
)
from modular_assembly.attribute.models import Attribute
from modular_assembly.atomic.serializers import (
    AtomicPrerequisiteSerializer
)

from modular_assembly.assembly.serializers import (
    ProductPrerequisiteSerializer,
)


class GasSpringAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = (
            ['key', 'value']
        )


class GasSpringBlueprintSerializer(serializers.ModelSerializer):

    atomic_prerequisites = AtomicPrerequisiteSerializer(many=True, read_only=False)
    product_prerequisites = ProductPrerequisiteSerializer(many=True, read_only=False)
    attribute = GasSpringAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Blueprint
        fields = (
            ['id', 'name', 'atomic_prerequisites', 'product_prerequisites', 'attribute']
        )


class ConfiguratorStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfiguratorStep
        fields = (
            ['id', 'title', 'description', 'type', 'slug', 'selected']
        )
