import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent
from shop.assembly.models import Blueprint


class AtomicComponentTests(APITestCase):

    def setUp(self):
        self.valid_payload = {
            "name": "Table",
            "atomic_prerequisites": [
                {
                    "atomic_component": {
                        'stock_code': 'p_bolt',
                        'part_code': 'p_bolt',
                        'description': 'General purpose Philip bolt',
                        'warehouse_location': '2000',
                        'weight': 3,
                        'image': '/img/bolt.png',
                        'availability': 6000,
                    },
                    "min_quantity": 1,
                    "max_quantity": 1,
                }
            ],
            "product_prerequisites": []
        }
        # self.invalid_payload = {
        #     'part_code': 'p_bolt',
        #     'description': 'General purpose Philip bolt',
        #     'warehouse_location': '2000',
        #     'weight': 3,
        #     'image': '/img/bolt.png',
        # }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = '/assembly/blueprint/create/'
        data = json.dumps(self.valid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blueprint.objects.count(), 1)
        # self.assertEqual(AtomicComponent.objects.get().stock_code, 'p_bolt')
