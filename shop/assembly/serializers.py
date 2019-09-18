from rest_framework import serializers
from shop.assembly.models import (
    Blueprint,
    Product,
    ProductPrerequisite,
    ProductSpecification,
)

from shop.atomic.models import AtomicPrerequisite
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

    atomic_prerequisites = AtomicPrerequisiteSerializer(many=True)
    product_prerequisites = ProductPrerequisiteSerializer(many=True)

    class Meta:
        model = Blueprint
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        atomic_prerequisites_data = validated_data.pop('atomic_prerequisites')
        product_prerequisites_data = validated_data.pop('product_prerequisites')
        blueprint = Blueprint.objects.create(**validated_data)
        for ap_data in atomic_prerequisites_data:
            print(atomic_prerequisites_data)
            AtomicPrerequisite.objects.create(**ap_data)
        for pp_data in product_prerequisites_data:
            ProductPrerequisite.objects.create(**pp_data)
        return blueprint


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = (
#             '__all__'
#         )



