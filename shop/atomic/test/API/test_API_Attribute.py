import json
from rest_framework.test import APITestCase
from rest_framework import status
from shop.attribute.models import Attribute


class AttributeTestCase(APITestCase):

    def test(self):
        """
        Test creating attribute within atomic component creation
        :return:
        """

        self.URL_VERSION = '/api/v1'

        tableTop = {
            'stock_code': 'TBT',
            'description': 'IKEA TABLE TOP',
            'warehouse_location': '2000',
            'weight': 100,
            'image': '/img/table_top.png',
            'availability': 80,
            'attribute': [
                {
                    'key': 'TEST_KEY',
                    'value': 'TEST_VALUE'
                }
            ]
        }

        url = self.URL_VERSION + '/atomic/component/create/'
        data = json.dumps(tableTop)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Attribute.objects.first().key, 'TEST_KEY')
        self.assertEqual(Attribute.objects.first().value, 'TEST_VALUE')

