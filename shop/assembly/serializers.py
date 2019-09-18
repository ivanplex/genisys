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

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductPrerequisite
        fields = (
            '__all__'
        )


class BlueprintSerializer(serializers.ModelSerializer):

    atomic_prerequisites = AtomicPrerequisiteSerializer(many=True, read_only=False)
    product_prerequisites = ProductPrerequisiteSerializer(many=True, read_only=False)

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
            a = AtomicPrerequisite.objects.create(**ap_data)
            blueprint.atomic_prerequisites.add(a)
        for pp_data in product_prerequisites_data:
            p = ProductPrerequisite.objects.create(**pp_data)
            blueprint.product_prerequisites.add(p)
        blueprint.save()
        return blueprint


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = (
#             '__all__'
#         )



