from django.test import TestCase
from django.core.exceptions import ValidationError

from shop.atomic.models import AtomicPrerequisite




# class AtomicComponent_PositiveAvailability_TestCase(TestCase):
#     def test(self):
#         """
#         Test AtomicComponent creation
#         """
#         a = AtomicComponent.objects.create(stock_code="LargeSupply", availability=30)
#         req = AtomicRequirement.objects.create(atomic_component=a, quantity=4)
#         self.assertEqual(req.available(), True)
#
# class AtomicComponent_NegativeAvailability_TestCase(TestCase):
#
#     def test(self):
#         """
#         Test AtomicComponent creation
#         """
#         a = AtomicComponent.objects.create(stock_code="LargeSupply", availability=3)
#         req = AtomicRequirement.objects.create(atomic_component=a, quantity=40)
#         self.assertEqual(req.available(), False)
