from rest_framework import serializers
from shop.assembly.models import Product
from shop.eCommerce.models import ECOMProduct, ECOMProductImage


class ECOMProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ECOMProductImage
        fields = (
            ['image_link']
        )


class ECOMProductSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    image_link = ECOMProductImageSerializer()
    additional_image_link = ECOMProductImageSerializer(many=True, read_only=False)

    class Meta:
        model = ECOMProduct
        fields = (
            '__all__'
        )
