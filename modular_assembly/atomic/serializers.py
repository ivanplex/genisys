from rest_framework import serializers
from modular_assembly.models import URL, OffsetImageURL
from modular_assembly.atomic.models import (
    AtomicComponent,
    AtomicPrerequisite,
    AtomicSpecification,
    AtomicGroup
)
from modular_assembly.attribute.models import Attribute
from modular_assembly.attribute.serializers import AttributeSerializer
from modular_assembly.serializers import (
    URLsSerializer,
    OffsetImageURLSerializer
)


class AtomicComponentSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)
    warehouse_location = serializers.CharField(required=False)
    material = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False)
    attribute = AttributeSerializer(many=True, read_only=False, required=False)
    image_urls = URLsSerializer(many=True, read_only=False, required=False)
    offset_image_urls = OffsetImageURLSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = AtomicComponent
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        atomic_component = AtomicComponent.objects.create(**validated_data)
        if 'attribute' in validated_data:
            attribute_data = validated_data.pop('attribute')
            for attribute in attribute_data:
                attr = Attribute.objects.create(**attribute)
                atomic_component.attribute.add(attr)
        # Save all URLs
        if 'image_urls' in validated_data:
            url_data = validated_data.pop('image_urls')
            for url in url_data:
                urlobject = URL.objects.create(**url)
                atomic_component.image_urls.add(urlobject)
        # Save all offset URLs
        if 'offset_image_urls' in validated_data:
            url_data = validated_data.pop('offset_image_urls')
            for url in url_data:
                urlobject = OffsetImageURL.objects.create(**url)
                atomic_component.offset_image_urls.add(urlobject)
        atomic_component.save()
        return atomic_component


class AtomicComponentConfiguratorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='sku')
    thumbnail_image = serializers.CharField(source='thumbnail_image.url', read_only=True)
    illustration_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)
    description_images = OffsetImageURLSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = AtomicComponent
        fields = (
            ['id',
             'name',
             'thumbnail_image',
             'illustration_images',
             'description_images',
             'retail_price',
             'retail_price_per_unit',
             'retail_unit_measurement',
             'component_factor',
             'length_on_ruler_offset',
             'availability'
             ]
        )


class AtomicPrerequisiteSerializer(serializers.ModelSerializer):

    atomic_component = serializers.PrimaryKeyRelatedField(queryset=AtomicComponent.objects.all(), required=False)
    atomic_group = serializers.PrimaryKeyRelatedField(queryset=AtomicGroup.objects.all(), required=False)

    class Meta:
        model = AtomicPrerequisite
        fields = (
            '__all__'
        )


class AtomicSpecificationSerializer(serializers.ModelSerializer):

    selected_component = serializers.PrimaryKeyRelatedField(queryset=AtomicComponent.objects.all())
    prerequisite = serializers.PrimaryKeyRelatedField(queryset=AtomicPrerequisite.objects.all())

    class Meta:
        model = AtomicSpecification
        fields = (
            '__all__'
        )
