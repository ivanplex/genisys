from rest_framework import serializers
from shop.models import URL


class URLsSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = (
            ['url']
        )
