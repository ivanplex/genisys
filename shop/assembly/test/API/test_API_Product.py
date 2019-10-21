import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import (
    AtomicComponent,
    AtomicPrerequisite,
    AtomicSpecification,
)
from shop.assembly.models import (
    Blueprint,
    Product,
)
from shop.assembly.serializers import ProductSerializer


class ProductTests(APITestCase):

    def setUp(self):

        self.URL_VERSION = '/api/v1'

        self.blueprint_table = Blueprint.objects.create(name="Table")
        self.atom_table_top = AtomicComponent.objects.create(
            stock_code="table_top",
            description="table top surface",
            warehouse_location="2001",
            material="wood",
            weight=450,
            image="/img/table_top.png",
            availability=2,
        )
        self.atom_leg = AtomicComponent.objects.create(
            stock_code="table_leg",
            description="legs",
            warehouse_location="2002",
            material="wood",
            weight=180,
            image="/img/leg.png",
            availability=10,
        )
        self.table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.atom_table_top, min_quantity=1, max_quantity=1)
        self.table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.atom_leg, min_quantity=4, max_quantity=4)
        self.atom_prereq = [self.table_AP_1, self.table_AP_2]
        for req in self.atom_prereq:
            self.blueprint_table.atomic_prerequisites.add(req)
        self.blueprint_table.save()

        self.valid_payload = {
            "name": "TableProduct",
            "sku": "tbl",
            "availability": 0,
            "blueprint": self.blueprint_table.id,
            "atomic_specifications": [
                {
                    "selected_component": AtomicComponent.objects.filter(stock_code="table_top").first().id,
                    "prerequisite": self.table_AP_1.id,
                    "quantity": 1,
                },
                {
                    "selected_component": AtomicComponent.objects.filter(stock_code="table_leg").first().id,
                    "prerequisite": self.table_AP_2.id,
                    "quantity": 4,
                }
            ],
            "product_specifications": []
        }

        self.invalid_payload = {
            "name": "TableProduct",
            "sku": "tbl",
            "availability": 0,
            "blueprint": self.blueprint_table.id,
            "atomic_specifications": [
                {
                    "hmm": "no luck",
                    "quantity": 1,
                },
            ],
            "product_specifications": []
        }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = self.URL_VERSION + '/assembly/product/create/'
        data = json.dumps(self.valid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'TableProduct')

    def test_invalid_create(self):
        """
        Missing specification
        """
        url = self.URL_VERSION + '/assembly/product/create/'
        data = json.dumps(self.invalid_payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view(self):
        product = Product.objects.create(name="table", blueprint=self.blueprint_table)
        self.table_AS_1 = AtomicSpecification.objects.create(
            selected_component=AtomicComponent.objects.filter(stock_code="table_top").first(),
            prerequisite=self.table_AP_1, quantity=1)
        self.table_AS_2 = AtomicSpecification.objects.create(
            selected_component=AtomicComponent.objects.filter(stock_code="table_leg").first(),
            prerequisite=self.table_AP_2, quantity=4)
        product.atomic_specifications.add(self.table_AS_1)
        product.atomic_specifications.add(self.table_AS_2)
        product.save()
        response = self.client.get(self.URL_VERSION + f'/assembly/product/view/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, ProductSerializer(instance=product).data)

    def test_delete(self):
        product = Product.objects.create(name="table", blueprint=self.blueprint_table)
        self.table_AS_1 = AtomicSpecification.objects.create(
            selected_component=AtomicComponent.objects.filter(stock_code="table_top").first(),
            prerequisite=self.table_AP_1, quantity=1)
        self.table_AS_2 = AtomicSpecification.objects.create(
            selected_component=AtomicComponent.objects.filter(stock_code="table_leg").first(),
            prerequisite=self.table_AP_2, quantity=4)
        product.atomic_specifications.add(self.table_AS_1)
        product.atomic_specifications.add(self.table_AS_2)
        product.save()
        response = self.client.delete(self.URL_VERSION + f'/assembly/product/delete/{product.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)

    def test_update(self):
        product = Product.objects.create(name="table", blueprint=self.blueprint_table)
        self.table_AS_1 = AtomicSpecification.objects.create(
            selected_component=AtomicComponent.objects.filter(stock_code="table_top").first(),
            prerequisite=self.table_AP_1, quantity=1)
        self.table_AS_2 = AtomicSpecification.objects.create(
            selected_component=AtomicComponent.objects.filter(stock_code="table_leg").first(),
            prerequisite=self.table_AP_2, quantity=4)
        product.atomic_specifications.add(self.table_AS_1)
        product.atomic_specifications.add(self.table_AS_2)
        product.save()
        response = self.client.patch(self.URL_VERSION + f'/assembly/product/update/{product.id}/', data={'name': 'chair'})
        product.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product.name, 'chair')

