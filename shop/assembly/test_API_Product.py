import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import (
    AtomicComponent,
    AtomicPrerequisite,
)
from shop.assembly.models import (
    Blueprint,
    Product,
)
from shop.assembly.serializers import BlueprintSerializer


class ProductTests(APITestCase):

    def setUp(self):
        blueprint_table = Blueprint.objects.create(name="Table")
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
        table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=atom_table_top, min_quantity=1, max_quantity=1)
        table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=atom_leg, min_quantity=4, max_quantity=4)
        atom_prereq = [table_AP_1, table_AP_2]
        for req in atom_prereq:
            blueprint_table.atomic_prerequisites.add(req)
        blueprint_table.save()

        self.valid_payload = {
            "name": "TableProduct",
            "sku": "tbl",
            "availability": 0,
            "blueprint": blueprint_table.id,
            "atomic_specifications": [
                {
                    "atomic_prereq": table_AP_1.id,
                    "quantity": 1,
                },
                {
                    "atomic_prereq": table_AP_2.id,
                    "quantity": 4,
                }
            ],
            "product_specifications": []
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
        url = '/assembly/product/create/'
        data = json.dumps(self.valid_payload)
        print(data)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'TableProduct')

    # def test_invalid_create(self):
    #     """
    #     Invalid creation
    #     Payload contains invalid prerequisite which is created
    #     simultaneously
    #     """
    #     url = '/assembly/blueprint/create/'
    #     data = json.dumps(self.invalid_payload)
    #     response = self.client.post(url, data, content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #
    # def test_view(self):
    #     blueprint = Blueprint.objects.create(name="table")
    #     response = self.client.get(f'/assembly/blueprint/view/{blueprint.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, BlueprintSerializer(instance=blueprint).data)
    #
    # def test_delete(self):
    #     blueprint = Blueprint.objects.create(name="table")
    #     response = self.client.delete(f'/assembly/blueprint/delete/{blueprint.id}/')
    #     self.assertEqual(response.status_code, 204)
    #     self.assertEqual(Blueprint.objects.count(), 0)
    #
    # def test_update(self):
    #     blueprint = Blueprint.objects.create(name="table")
    #     response = self.client.patch(f'/assembly/blueprint/update/{blueprint.id}/', data={'name': 'chair'})
    #     blueprint.refresh_from_db()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(blueprint.name, 'chair')
    #
