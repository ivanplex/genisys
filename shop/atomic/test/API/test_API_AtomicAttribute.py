import json
from rest_framework.test import APITestCase
from rest_framework import status


class AtomicAttributeTestCase(APITestCase):

    def test(self):

        self.URL_VERSION = '/api/v1'

        tableTop = {
            'stock_code': 'TBT',
            'description': 'IKEA TABLE TOP',
            'warehouse_location': '2000',
            'weight': 100,
            'image': '/img/table_top.png',
            'availability': 80,
        }

        url = self.URL_VERSION + '/atomic/component/create/'
        data = json.dumps(tableTop)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
