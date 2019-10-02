from rest_framework import serializers
from shop.group.models import AtomicGroup, BlueprintGroup, ProductGroup
from shop.atomic.serializers import AtomicComponentSerializer
from shop.assembly.serializers import ProductSerializer, BlueprintSerializer


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
