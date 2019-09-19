import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent
from shop.assembly.models import Blueprint
from shop.assembly.serializers import BlueprintSerializer


class BlueprintTests(APITestCase):

    def test_create_table_set(self):
        atom_table_top = json.dumps({
            'stock_code': 'table_top',
            'part_code': 'table_top',
            'description': 'Just a table top',
            'warehouse_location': '2001',
            'material': 'wood',
            'weight': 450,
            'image': '/img/table_top.png',
            'availability': 2,
        })

        atom_table_leg = json.dumps({
            'stock_code': 'table_leg',
            'part_code': 'table_leg',
            'description': 'Just some table leg',
            'warehouse_location': '2002',
            'material': 'wood',
            'weight': 180,
            'image': '/img/table_leg.png',
            'availability': 20,
        })

        url = '/atomic/component/create/'

        # Send request: CREATE TABLE TOP
        response = self.client.post(url, atom_table_top, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Send request: CREATE TABLE LEG
        response = self.client.post(url, atom_table_leg, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        blueprint_table = json.dumps({
            "name": "Table",
            "atomic_prerequisites": [
                {
                    "atomic_component": 1,
                    "min_quantity": 1,
                    "max_quantity": 1,
                },
                {
                    "atomic_component": 2,
                    "min_quantity": 4,
                    "max_quantity": 4,
                }
            ],
            "product_prerequisites": []
        })

        # Send request: CREATE TABLE BLUEPRINT
        response = self.client.post(url, blueprint_table, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
