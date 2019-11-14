from rest_framework import serializers
from shop.models import URL, OffsetImageURL
from shop.serializers import URLsSerializer
from shop.assembly.models import (
    Blueprint,
    Product,
    ProductPrerequisite,
    ProductSpecification,
)

from shop.atomic.models import (
    AtomicPrerequisite,
    AtomicSpecification,
)

from shop.atomic.serializers import (
    AtomicPrerequisiteSerializer,
    AtomicSpecificationSerializer,
)
from shop.attribute.models import Attribute
from shop.attribute.serializers import AttributeSerializer
from shop.serializers import (
    URLsSerializer,
    OffsetImageURLSerializer
)


class ProductPrerequisiteSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductPrerequisite
        fields = (
            '__all__'
        )


class ProductSpecificationSerializer(serializers.ModelSerializer):

    selected_component = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    prerequisite = serializers.PrimaryKeyRelatedField(queryset=ProductPrerequisite.objects.all())

    class Meta:
        model = ProductSpecification
        fields = (
            '__all__'
        )


class BlueprintConfiguratorSerializer(serializers.ModelSerializer):
    thumbnail_image = URLsSerializer(read_only=False, required=False)
    illustration_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)
    description_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Blueprint
        fields = (
            ['id',
             'name',
             'thumbnail_image',
             'illustration_images',
             'description_images',
             'retail_price',
             'retail_price_per_unit',
             'retail_unit_measurement'
             ]
        )


class BlueprintSerializer(serializers.ModelSerializer):

    atomic_prerequisites = AtomicPrerequisiteSerializer(many=True, read_only=False)
    product_prerequisites = ProductPrerequisiteSerializer(many=True, read_only=False)
    thumbnail_image = URLsSerializer(read_only=False, required=False)
    illustration_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)
    description_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Blueprint
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        atomic_prerequisites_data = validated_data.pop('atomic_prerequisites')
        product_prerequisites_data = validated_data.pop('product_prerequisites')
        blueprint = Blueprint.objects.create(**validated_data)
        # save all atomic prerequisites
        for ap_data in atomic_prerequisites_data:
            a = AtomicPrerequisite.objects.create(**ap_data)
            blueprint.atomic_prerequisites.add(a)
        # save all product prerequisite
        for pp_data in product_prerequisites_data:
            p = ProductPrerequisite.objects.create(**pp_data)
            blueprint.product_prerequisites.add(p)
        # Save all URLs
        if 'image_urls' in validated_data:
            url_data = validated_data.pop('image_urls')
            for url in url_data:
                urlobject = URL.objects.create(**url)
                blueprint.image_urls.add(urlobject)
        # Save all offset URLs
        if 'offset_image_urls' in validated_data:
            url_data = validated_data.pop('offset_image_urls')
            for url in url_data:
                urlobject = OffsetImageURL.objects.create(**url)
                blueprint.offset_image_urls.add(urlobject)
        blueprint.save()
        return blueprint


class ProductSerializer(serializers.ModelSerializer):

    blueprint = serializers.PrimaryKeyRelatedField(queryset=Blueprint.objects.all())
    atomic_specifications = AtomicSpecificationSerializer(many=True, read_only=False)
    product_specifications = ProductSpecificationSerializer(many=True, read_only=False)
    attribute = AttributeSerializer(many=True, read_only=False, required=False)
    thumbnail_image = URLsSerializer(read_only=False, required=False)
    illustration_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)
    description_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Product
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        atomic_specifications_data = validated_data.pop('atomic_specifications')
        product_specifications_data = validated_data.pop('product_specifications')
        product = Product.objects.create(**validated_data)
        # save all atomic specifications
        for as_data in atomic_specifications_data:
            a = AtomicSpecification.objects.create(**as_data)
            product.atomic_specifications.add(a)
        # Save all product specifications
        for ps_data in product_specifications_data:
            p = ProductSpecification.objects.create(**ps_data)
            product.product_specifications.add(p)
        # Save all attributes
        if 'attribute' in validated_data:
            attribute_data = validated_data.pop('attribute')
            for attribute in attribute_data:
                attr = Attribute.objects.create(**attribute)
                product.attribute.add(attr)
        # Save all URLs
        if 'image_urls' in validated_data:
            url_data = validated_data.pop('image_urls')
            for url in url_data:
                urlobject = URL.objects.create(**url)
                product.image_urls.add(urlobject)
        # Save all offset URLs
        if 'offset_image_urls' in validated_data:
            url_data = validated_data.pop('offset_image_urls')
            for url in url_data:
                urlobject = OffsetImageURL.objects.create(**url)
                product.offset_image_urls.add(urlobject)
        product.save()
        return product
