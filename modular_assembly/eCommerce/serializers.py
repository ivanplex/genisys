from rest_framework import serializers
from modular_assembly.assembly.models import Product
from modular_assembly.eCommerce.models import ECOMProduct, ECOMProductImage


# class ECOMProductImageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ECOMProductImage
#         fields = (
#             ['image_link']
#         )


class ECOMProductImageSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return value.image_link

    class Meta:
        model = ECOMProductImage
        fields = (
            ['image_link']
        )




class ECOMProductSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    additional_image_link = ECOMProductImageSerializer(many=True, read_only=True)
    # image_link = ECOMProductImageSerializer()
    # additional_image_link = ECOMProductImageSerializer(many=True, read_only=False)

    class Meta:
        model = ECOMProduct
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        additional_image_data = validated_data.pop('additional_image_link')
        ecom_product = ECOMProduct.objects.create(**validated_data)
        for additional_image in additional_image_data:
            url, created = ECOMProductImage.objects.get_or_create(**additional_image)
        return ecom_product
