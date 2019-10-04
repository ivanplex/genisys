import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.assembly.models import Blueprint, BlueprintAttribute
from shop.assembly.serializers import BlueprintAttributeSerializer


class BlueprintAttributeAPITests(APITestCase):

    def setUp(self):
        self.blueprint = Blueprint.objects.create(name="Table")
        self.payload = {
            "blueprint": self.blueprint.id,
            "key": "TESTKEY",
            "value": "TESTVALUE"
        }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = '/attribute/blueprint/create/'
        data = json.dumps(self.payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlueprintAttribute.objects.count(), 1)

    def test_view(self):
        attribute = BlueprintAttribute.objects.create(blueprint=self.blueprint, key='TESTKEY', value='TESTVALUE')
        response = self.client.get(f'/attribute/blueprint/view/{attribute.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, BlueprintAttributeSerializer(instance=attribute).data)

    def test_delete(self):
        attribute = BlueprintAttribute.objects.create(blueprint=self.blueprint, key='TESTKEY', value='TESTVALUE')
        response = self.client.delete(f'/attribute/blueprint/delete/{attribute.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(BlueprintAttribute.objects.count(), 0)

    def test_update(self):
        attribute = BlueprintAttribute.objects.create(blueprint=self.blueprint, key='TESTKEY', value='TESTVALUE')
        response = self.client.patch(f'/attribute/blueprint/update/{attribute.id}/', data={'value': 'NEWVALUE'})
        attribute.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(attribute.get_value(), 'NEWVALUE')

