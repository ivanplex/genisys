from rest_framework import serializers
from shop.assembly.models import (
    Blueprint,
    Product,
    ProductPrerequisite,
    ProductSpecification,
)

from shop.atomic.serializers import (
    AtomicPrerequisiteSerializer
)


class ProductPrerequisiteSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductPrerequisite
        fields = (
            '__all__'
        )


class BlueprintSerializer(serializers.ModelSerializer):

    atomic_prerequisites = AtomicPrerequisiteSerializer(many=True, read_only=True)
    product_prerequisites = ProductPrerequisiteSerializer(many=True, read_only=True)

    class Meta:
        model = Blueprint
        fields = (
            '__all__'
        )


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = (
#             '__all__'
#         )



