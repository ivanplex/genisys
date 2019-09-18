import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent
from shop.assembly.models import Blueprint


class AtomicComponentTests(APITestCase):

    def setUp(self):
        atom_table_top = AtomicComponent.objects.create(
            stock_code="table_top",
            part_code="",
            description="table top surface",
            warehouse_location="2001",
            material="wood",
            weight=450,
            image="/img/table_top.png",
            availability=2,
        )
        atom_leg = AtomicComponent.objects.create(
            stock_code="table_leg",
            part_code="",
            description="legs",
            warehouse_location="2002",
            material="wood",
            weight=180,
            image="/img/leg.png",
            availability=10,
        )

        self.valid_payload = {
            "name": "Table",
            "atomic_prerequisites": [
                {
                    "atomic_component": atom_table_top.id,
                    "min_quantity": 1,
                    "max_quantity": 1,
                },
                {
                    "atomic_component": atom_leg.id,
                    "min_quantity": 4,
                    "max_quantity": 4,
                }
            ],
            "product_prerequisites": []
        }

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
