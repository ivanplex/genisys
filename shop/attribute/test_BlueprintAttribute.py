from rest_framework.test import APITestCase

from shop.assembly.models import Blueprint
from .models import BlueprintAttribute


class BlueprintAttributeTestCase(APITestCase):

    def setUp(self):
        self.blueprint = Blueprint.objects.create('Table')

    def test_creation(self):
        attr = BlueprintAttribute(blueprint=self.blueprint, key='color', value='white')
        self.assertEqual(attr.get_key(), 'color')
        self.assertEqual(attr.get_value(), 'white')
