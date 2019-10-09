import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent
from shop.assembly.models import Blueprint
from shop.assembly.serializers import BlueprintSerializer


class BlueprintTests(APITestCase):

    def setUp(self):

        self.URL_VERSION = '/api/v1'

        atom_table_top = AtomicComponent.objects.create(
            stock_code="table_top",
            description="table top surface",
            warehouse_location="2001",
            material="wood",
            weight=450,
            image="/img/table_top.png",
            availability=2,
        )
        atom_leg = AtomicComponent.objects.create(
            stock_code="table_leg",
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

        self.invalid_payload = {
            "name": "Table",
            "atomic_prerequisites": [
                {
                    "unknown": "parameter",
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
        url = self.URL_VERSION + '/assembly/blueprint/create/'
        data = json.dumps(self.valid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blueprint.objects.count(), 1)
        self.assertEqual(Blueprint.objects.get().name, 'Table')

    def test_invalid_create(self):
        """
        Invalid creation
        Payload contains invalid prerequisite which is created
        simultaneously
        """
        url = self.URL_VERSION + '/assembly/blueprint/create/'
        data = json.dumps(self.invalid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view(self):
        blueprint = Blueprint.objects.create(name="table")
        response = self.client.get(self.URL_VERSION + f'/assembly/blueprint/view/{blueprint.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, BlueprintSerializer(instance=blueprint).data)

    def test_delete(self):
        blueprint = Blueprint.objects.create(name="table")
        response = self.client.delete(self.URL_VERSION + f'/assembly/blueprint/delete/{blueprint.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Blueprint.objects.count(), 0)

    def test_update(self):
        blueprint = Blueprint.objects.create(name="table")
        response = self.client.patch(self.URL_VERSION + f'/assembly/blueprint/update/{blueprint.id}/', data={'name': 'chair'})
        blueprint.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(blueprint.name, 'chair')

