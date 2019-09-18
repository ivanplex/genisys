import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent
from shop.atomic.serializers import AtomicComponentSerializer


class AtomicComponentTests(APITestCase):

    def setUp(self):
        self.valid_payload = {
            'stock_code': 'p_bolt',
            'part_code': 'p_bolt',
            'description': 'General purpose Philip bolt',
            'warehouse_location': '2000',
            'weight': 3,
            'image': '/img/bolt.png',
            'availability': 6000,
        }
        self.invalid_payload = {
            'part_code': 'p_bolt',
            'description': 'General purpose Philip bolt',
            'warehouse_location': '2000',
            'weight': 3,
            'image': '/img/bolt.png',
        }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = '/atomic/component/create/'
        data = json.dumps(self.valid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AtomicComponent.objects.count(), 1)
        self.assertEqual(AtomicComponent.objects.get().stock_code, 'p_bolt')

    def test_invalid_create(self):
        """
        Test create with missing required field
        """
        url = '/atomic/component/create/'
        data = json.dumps(self.invalid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view(self):
        atom = AtomicComponent.objects.create(
            stock_code="p_bolt",
            part_code="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        response = self.client.get(f'/atomic/component/view/{atom.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, AtomicComponentSerializer(instance=atom).data)

    def test_delete(self):
        atom = AtomicComponent.objects.create(
            stock_code="p_bolt",
            part_code="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        response = self.client.delete(f'/atomic/component/delete/{atom.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(AtomicComponent.objects.count(), 0)

    def test_update(self):
        atom = AtomicComponent.objects.create(
            stock_code="p_bolt",
            part_code="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        response = self.client.patch(f'/atomic/component/update/{atom.id}/', data={'material': 'Steel'})
        atom.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(atom.material, 'Steel')
