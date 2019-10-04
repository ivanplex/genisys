from rest_framework.test import APITestCase

from shop.atomic.models import AtomicComponent, AtomicAttribute


class AtomAttributeTestCase(APITestCase):

    def setUp(self):
        self.atom = AtomicComponent.objects.create(stock_code='screw')
        self.attr_1 = AtomicAttribute.objects.create(atomic_component=self.atom, key='length', value='500')
        self.attr_2 = AtomicAttribute.objects.create(atomic_component=self.atom, key='color', value='black')

    def test_creation(self):
        self.assertEqual(self.attr_1.get_key(), 'length')
        self.assertEqual(self.attr_1.get_value(), '500')
