from rest_framework import serializers
from shop.assembly.models import BlueprintGroup, ProductGroup
from shop.atomic.models import AtomicGroup
from shop.atomic.serializers import AtomicComponentSerializer
from shop.assembly.serializers import ProductSerializer, BlueprintSerializer
from shop.group.models import Group
from shop.serializers import (
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
