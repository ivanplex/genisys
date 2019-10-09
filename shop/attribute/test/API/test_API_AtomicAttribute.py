import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent, AtomicAttribute
from shop.atomic.serializers import AtomicAttributeSerializer


class AtomicAttributeAPITests(APITestCase):

    def setUp(self):

        self.URL_VERSION = '/api/v1'

        self.atom = AtomicComponent.objects.create(
            stock_code="table_top",
            description="table top surface",
            warehouse_location="2001",
            material="wood",
            weight=450,
            image="/img/table_top.png",
            availability=2,
        )
        self.payload = {
            "atomic_component": self.atom.id,
            "key": "color",
            "value": "white"
        }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = self.URL_VERSION + '/attribute/atomic/create/'
        data = json.dumps(self.payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AtomicAttribute.objects.count(), 1)

    def test_view(self):
        attribute = AtomicAttribute.objects.create(atomic_component=self.atom, key='color', value='white')
        response = self.client.get(self.URL_VERSION + f'/attribute/atomic/view/{attribute.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, AtomicAttributeSerializer(instance=attribute).data)

    def test_delete(self):
        attribute = AtomicAttribute.objects.create(atomic_component=self.atom, key='color', value='white')
        response = self.client.delete(self.URL_VERSION + f'/attribute/atomic/delete/{attribute.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(AtomicAttribute.objects.count(), 0)

    def test_update(self):
        attribute = AtomicAttribute.objects.create(atomic_component=self.atom, key='color', value='white')
        response = self.client.patch(self.URL_VERSION + f'/attribute/atomic/update/{attribute.id}/', data={'value': 'black'})
        attribute.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(attribute.get_value(), 'black')

