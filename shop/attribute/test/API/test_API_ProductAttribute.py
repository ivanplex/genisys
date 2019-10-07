import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.assembly.models import Blueprint, Product, ProductAttribute
from shop.assembly.serializers import ProductAttributeSerializer


class ProductAttributeAPITests(APITestCase):

    def setUp(self):

        self.URL_VERSION = '/api/v1'

        blueprint = Blueprint.objects.create(name="Table")
        self.product = Product.objects.create(name="Table", sku="TBL", blueprint=blueprint)
        self.payload = {
            "product": self.product.id,
            "key": "TESTKEY",
            "value": "TESTVALUE"
        }

    def test_create(self):
        """
        Ensure we can create AtomicComponent
        """
        url = self.URL_VERSION + '/attribute/product/create/'
        data = json.dumps(self.payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductAttribute.objects.count(), 1)

    def test_view(self):
        attribute = ProductAttribute.objects.create(product=self.product, key='TESTKEY', value='TESTVALUE')
        response = self.client.get(self.URL_VERSION + f'/attribute/product/view/{attribute.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, ProductAttributeSerializer(instance=attribute).data)

    def test_delete(self):
        attribute = ProductAttribute.objects.create(product=self.product, key='TESTKEY', value='TESTVALUE')
        response = self.client.delete(self.URL_VERSION + f'/attribute/product/delete/{attribute.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ProductAttribute.objects.count(), 0)

    def test_update(self):
        attribute = ProductAttribute.objects.create(product=self.product, key='TESTKEY', value='TESTVALUE')
        response = self.client.patch(self.URL_VERSION + f'/attribute/product/update/{attribute.id}/', data={'value': 'NEWVALUE'})
        attribute.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(attribute.get_value(), 'NEWVALUE')
