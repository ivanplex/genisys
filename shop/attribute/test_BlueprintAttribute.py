from rest_framework.test import APITestCase

from shop.assembly.models import Blueprint, BlueprintAttribute


class BlueprintAttributeTestCase(APITestCase):

    def setUp(self):
        self.blueprint = Blueprint.objects.create(name='table')
        self.attr_1 = BlueprintAttribute.objects.create(blueprint=self.blueprint, key='width', value='500')
        self.attr_2 = BlueprintAttribute.objects.create(blueprint=self.blueprint, key='color', value='black')

    def test_creation(self):
        self.assertEqual(self.attr_1.get_key(), 'width')
        self.assertEqual(self.attr_1.get_value(), '500')

    def test_fetch(self):
        print(self.blueprint.attribute())
        self.assertTrue(True)
