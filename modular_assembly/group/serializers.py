from rest_framework import serializers
from modular_assembly.assembly.models import BlueprintGroup, ProductGroup
from modular_assembly.atomic.models import AtomicGroup
from modular_assembly.atomic.serializers import AtomicComponentSerializer
from modular_assembly.assembly.serializers import ProductSerializer, BlueprintSerializer
from modular_assembly.group.models import Group
from modular_assembly.serializers import (
    URLsSerializer,
    OffsetImageURLSerializer
)

class GroupSerializer(serializers.ModelSerializer):

    thumbnail_image = serializers.CharField(source='thumbnail_image.url', read_only=True)
    illustration_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)
    description_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Group
        fields = (
            ['id',
             'name',
             'thumbnail_image',
             'illustration_images',
             'description_images'
            ]
        )

class AtomicGroupSerializer(serializers.ModelSerializer):

    members = AtomicComponentSerializer(many=True, read_only=False)

    class Meta:
        model = AtomicGroup
        fields = (
            '__all__'
        )


class BlueprintGroupSerializer(serializers.ModelSerializer):

    members = BlueprintSerializer(many=True, read_only=False)

    class Meta:
        model = BlueprintGroup
        fields = (
            '__all__'
        )


class ProductGroupSerializer(serializers.ModelSerializer):

    members = ProductSerializer(many=True, read_only=False)

    class Meta:
        model = ProductGroup
        fields = (
            '__all__'
        )
