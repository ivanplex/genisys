from rest_framework import serializers
from shop.group.models import AtomicGroup, ProductGroup
from shop.atomic.serializers import AtomicComponentSerializer
from shop.assembly.serializers import ProductSerializer


class AtomicGroupSerializer(serializers.ModelSerializer):

    members = AtomicComponentSerializer(many=True, read_only=False)

    class Meta:
        model = AtomicGroup
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
