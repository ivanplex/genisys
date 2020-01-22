"""
Test AtomicPrerequisites using API
"""

import json
from rest_framework.test import APITestCase
from rest_framework import status

from modular_assembly.atomic.models import AtomicComponent


class AtomicPrerequisiteTestCase(APITestCase):

    def setUp(self):

        self.URL_VERSION = '/api/v1'

        self.rod = AtomicComponent.objects.create(
            sku="rod",
            description="rod of a gas spring",
            warehouse_location="2001",
            material="steel",
            weight=80,
            image="",
            availability=2,
        )
        self.tube = AtomicComponent.objects.create(
            sku="tube",
            description="tube of a gas spring",
            warehouse_location="2003",
            material="steel",
            weight=90,
            image="",
            availability=6,
        )
        self.seal = AtomicComponent.objects.create(
            sku="seal",
            description="seal of a gas spring",
            warehouse_location="1000",
            material="rubber",
            weight=4,
            image="",
            availability=8000,
        )
        self.endfitting1 = AtomicComponent.objects.create(
            sku="endfitting1",
            description="endfitting of a gas spring",
            warehouse_location="30",
            material="steal",
            weight=20,
            image="",
            availability=50,
        )
        self.endfitting2 = AtomicComponent.objects.create(
            sku="endfitting2",
            description="endfitting of a gas spring",
            warehouse_location="31",
            material="steal",
            weight=20,
            image="",
            availability=50,
        )

    def test_baseline_create(self):
        """
        Create gas spring only
        """
        url = self.URL_VERSION + '/assembly/blueprint/create/'
        payload = {
            "name": "gas spring",
            "atomic_prerequisites": [
                {
                    "atomic_component": self.rod.id,
                    "required": True,
                    "min_quantity": 100000,  # 100mm
                    "max_quantity": 800000,  # 800mm
                },
                {
                    "atomic_component": self.tube.id,
                    "required": True,
                    "min_quantity": 100000,  # 100mm
                    "max_quantity": 800000,  # 800mm
                },
                {
                    "atomic_component": self.seal.id,
                    "required": True,
                    "min_quantity": 1,
                    "max_quantity": 1,
                }
            ],
            "product_prerequisites": []
        }
        data = json.dumps(payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_with_options(self):
        """
        Create Gas Sprint with optional endfitting
        """
        url = self.URL_VERSION + '/assembly/blueprint/create/'
        payload = {
            "name": "gas spring",
            "atomic_prerequisites": [
                {
                    "atomic_component": self.rod.id,
                    "min_quantity": 100000,  # 100mm
                    "max_quantity": 800000,  # 800mm
                },
                {
                    "atomic_component": self.tube.id,
                    "min_quantity": 100000,  # 100mm
                    "max_quantity": 800000,  # 800mm
                },
                {
                    "atomic_component": self.seal.id,
                    "min_quantity": 1,
                    "max_quantity": 1,
                },
                {
                    "atomic_component": self.endfitting1.id,
                    "min_quantity": 0,
                    "max_quantity": 1,
                },
                {
                    "atomic_component": self.endfitting2.id,
                    "min_quantity": 0,
                    "max_quantity": 1,
                }
            ],
            "product_prerequisites": []
        }
        data = json.dumps(payload)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
