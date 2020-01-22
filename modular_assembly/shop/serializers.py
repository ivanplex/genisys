from rest_framework import serializers
from shop.models import URL, OffsetImageURL


class URLsSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = (
            ['url']
        )


class OffsetImageURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = OffsetImageURL
        fields = (
            ['url', 'offset_x', 'offset_y']
        )
