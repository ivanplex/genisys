from rest_framework import serializers
from shop.attribute.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = (
            '__all__'
        )
