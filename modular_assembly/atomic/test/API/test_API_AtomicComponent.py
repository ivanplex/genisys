import json
from rest_framework.test import APITestCase
from rest_framework import status

from modular_assembly.atomic.models import AtomicComponent
from modular_assembly.atomic.serializers import AtomicComponentSerializer


class AtomicComponentTests(APITestCase):

    def setUp(self):

        self.URL_VERSION = '/api/v1'

        self.valid_payload = {
            'sku': 'p_bolt',
            'description': 'General purpose Philip bolt',
            'warehouse_location': '2000',
            'weight': 3,
            'image': '/img/bolt.png',
            'availability': 6000,
        }
        self.invalid_payload = {
            'description': 'General purpose Philip bolt',
            'warehouse_location': '2000',
            'weight': 3,
            'image': '/img/bolt.png',
            'availability': 6000,
        }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = self.URL_VERSION + '/atomic/component/create/'
        data = json.dumps(self.valid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AtomicComponent.objects.count(), 1)
        self.assertEqual(AtomicComponent.objects.get().sku, 'p_bolt')

    def test_invalid_create(self):
        """
        Test create with missing required field
        """
        url = self.URL_VERSION + '/atomic/component/create/'
        data = json.dumps(self.invalid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view(self):
        atom = AtomicComponent.objects.create(
            sku="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        response = self.client.get(self.URL_VERSION + f'/atomic/component/view/{atom.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, AtomicComponentSerializer(instance=atom).data)

    def test_delete(self):
        atom = AtomicComponent.objects.create(
            sku="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        response = self.client.delete(self.URL_VERSION + f'/atomic/component/delete/{atom.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(AtomicComponent.objects.count(), 0)

    def test_update(self):
        atom = AtomicComponent.objects.create(
            sku="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        response = self.client.patch(self.URL_VERSION + f'/atomic/component/update/{atom.id}/', data={'material': 'Steel'})
        atom.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(atom.material, 'Steel')
