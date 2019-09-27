from rest_framework.test import APITestCase

from shop.atomic.models import AtomicComponent
from .models import AtomicAttribute


class AtomAttributeTestCase(APITestCase):

    def setUp(self):
        self.atom = AtomicComponent.objects.create(stock_code='screw')

    def test_creation(self):
        attr = AtomicAttribute(atomic_component=self.atom, key='length', value='500')
        self.assertEqual(attr.get_key(), 'length')
        self.assertEqual(attr.get_value(), '500')
