"""
Test BlueprintPrerequisites using API
"""

import json
from rest_framework.test import APITestCase
from rest_framework import status

from shop.atomic.models import AtomicComponent


class BlueprintPrerequisiteTestCase(APITestCase):

    def submit(self, url, payload):
        data = json.dumps(payload)
        return self.client.post(url, data, content_type='application/json')

    def test_create_atomic_component(self):
        tableTop = {
            'stock_code': 'TBT',
            'part_code': 'tableTop',
            'description': 'IKEA TABLE TOP',
            'warehouse_location': '2000',
            'weight': 100,
            'image': '/img/table_top.png',
            'availability': 80,
        }
        tableLeg = {
            'stock_code': 'TBL',
            'part_code': 'tableLeg',
            'description': 'IKEA TABLE LEG',
            'warehouse_location': '2001',
            'weight': 40,
            'image': '/img/table_leg.png',
            'availability': 200,
        }
        screws = {
            'stock_code': 'SRW',
            'part_code': 'screw',
            'description': 'screws',
            'warehouse_location': '80000',
            'weight': 1,
            'image': '/img/screws.png',
            'availability': 100000,
        }
        chairPlate = {
            'stock_code': 'CPT',
            'part_code': 'chairPlate',
            'description': 'IKEA Chair Back plate',
            'warehouse_location': '7000',
            'weight': 120,
            'image': '/img/chair_back_plate.png',
            'availability': 20,
        }
        chairleg = {
            'stock_code': 'CLG',
            'part_code': 'chairLeg',
            'description': 'IKEA Chair Leg',
            'warehouse_location': '7001',
            'weight': 30,
            'image': '/img/chair_leg.png',
            'availability': 55,
        }
        manual = {
            'stock_code': 'MNU',
            'part_code': 'manual',
            'description': 'IKEA assembly manual',
            'warehouse_location': '1',
            'weight': 15,
            'image': '/img/manual.png',
            'availability': 30,
        }
        atomic_comp = [
            tableTop,
            tableLeg,
            chairPlate,
            chairleg,
            screws,
            manual
        ]

        #Create each atomic component using API calls
        for comp in atomic_comp:
            url = '/atomic/component/create/'
            response = self.submit(url, comp)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        print(AtomicComponent.objects.filter(stock_code='CEF'))

    def test_create_blueprint(self):
        tableTop = {
            'name': 'Table',
            'atomic_prerequisites': [
                {

                }
            ]
        }



    # def test_baseline_create(self):
    #     """
    #     Create gas spring only
    #     """
    #     url = '/assembly/blueprint/create/'
    #     payload = {
    #         "name": "gas spring",
    #         "atomic_prerequisites": [
    #             {
    #                 "atomic_component": self.rod.id,
    #                 "required": True,
    #                 "min_quantity": 100000,  # 100mm
    #                 "max_quantity": 800000,  # 800mm
    #             },
    #             {
    #                 "atomic_component": self.tube.id,
    #                 "required": True,
    #                 "min_quantity": 100000,  # 100mm
    #                 "max_quantity": 800000,  # 800mm
    #             },
    #             {
    #                 "atomic_component": self.seal.id,
    #                 "required": True,
    #                 "min_quantity": 1,
    #                 "max_quantity": 1,
    #             }
    #         ],
    #         "product_prerequisites": []
    #     }
    #     data = json.dumps(payload)
    #     response = self.client.post(url, data, content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_create_with_options(self):
    #     """
    #     Create Gas Sprint with optional endfitting
    #     """
    #     url = '/assembly/blueprint/create/'
    #     payload = {
    #         "name": "gas spring",
    #         "atomic_prerequisites": [
    #             {
    #                 "atomic_component": self.rod.id,
    #                 "min_quantity": 100000,  # 100mm
    #                 "max_quantity": 800000,  # 800mm
    #             },
    #             {
    #                 "atomic_component": self.tube.id,
    #                 "min_quantity": 100000,  # 100mm
    #                 "max_quantity": 800000,  # 800mm
    #             },
    #             {
    #                 "atomic_component": self.seal.id,
    #                 "min_quantity": 1,
    #                 "max_quantity": 1,
    #             },
    #             {
    #                 "atomic_component": self.endfitting1.id,
    #                 "min_quantity": 0,
    #                 "max_quantity": 1,
    #             },
    #             {
    #                 "atomic_component": self.endfitting2.id,
    #                 "min_quantity": 0,
    #                 "max_quantity": 1,
    #             }
    #         ],
    #         "product_prerequisites": []
    #     }
    #     data = json.dumps(payload)
    #     response = self.client.post(url, data, content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
