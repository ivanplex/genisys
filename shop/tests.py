import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent
from shop.assembly.models import Blueprint, Product


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

        atom_chair = json.dumps({
            'stock_code': 'chair',
            'part_code': 'chair',
            'description': 'c',
            'warehouse_location': '3000',
            'material': 'wood',
            'weight': 600,
            'image': '/img/chair.png',
            'availability': 15,
        })

        url = '/atomic/component/create/'

        # Send request: CREATE TABLE TOP
        response = self.client.post(url, atom_table_top, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Send request: CREATE TABLE LEG
        response = self.client.post(url, atom_table_leg, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Send request: CREATE CHAIR
        response = self.client.post(url, atom_chair, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        blueprint_table = json.dumps({
            "name": "Table",
            "atomic_prerequisites": [
                {
                    "atomic_component": AtomicComponent.objects.filter(stock_code='table_top').first().id,
                    "min_quantity": 1,
                    "max_quantity": 1,
                },
                {
                    "atomic_component": AtomicComponent.objects.filter(stock_code='table_leg').first().id,
                    "min_quantity": 4,
                    "max_quantity": 4,
                }
            ],
            "product_prerequisites": []
        })

        url = '/assembly/blueprint/create/'

        # Send request: CREATE TABLE BLUEPRINT
        response = self.client.post(url, blueprint_table, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Product Table
        product_table = json.dumps({
            "name": "Table",
            "sku": "tbl",
            "availability": 0,
            "blueprint": Blueprint.objects.filter(name="Table").first().id,
            "atomic_specifications": [
                {
                    "atomic_prereq": 1,
                    "quantity": 1,
                },
                {
                    "atomic_prereq": 2,
                    "quantity": 4,
                }
            ],
            "product_specifications": []
        })

        url = '/assembly/product/create/'

        # Send request: CREATE TABLE PRODUCT
        response = self.client.post(url, product_table, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        blueprint_table_set = json.dumps({
            "name": "Table-Set",
            "atomic_prerequisites": [
                {
                    "atomic_component": AtomicComponent.objects.filter(stock_code='chair').first().id,
                    "min_quantity": 2,
                    "max_quantity": 4,
                },
            ],
            "product_prerequisites": [
                {
                    "product": Product.objects.filter(name="Table").first().id,
                    "min_quantity": 1,
                    "max_quantity": 1,
                }
            ]
        })

        url = '/assembly/blueprint/create/'

        # Send request: CREATE TABLE BLUEPRINT
        response = self.client.post(url, blueprint_table_set, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
