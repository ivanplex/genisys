from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import AtomicComponent, AtomicRequirement, Blueprint, BlueprintRequirement

# Create your tests here.

class AtomicComponent_create_TestCase(TestCase):
    def test(self):
        """
        Test AtomicComponent creation
        """
        a = AtomicComponent()
        a.save()
        pass

# class BlueprintRequirement_SigularRequirement_NoneSupply_TestCase(TestCase):
#     """
#     Verify Blueprint requirement either require blueprint or atomic component
#     aka. cannot be both empty or both required
#     """
#     def test(self):
#         """Animals that can speak are correctly identified"""
#         try:
#             br = BlueprintRequirements(required_type='Atomic', quantity=1)
#             br.save()
#             self.fail("Violation of singular requirement")
#         except ValidationError:
#             pass
#
# class BlueprintRequirement_SigularRequirement_BothSupply_TestCase(TestCase):
#
#     def test(self):
#         """Animals that can speak are correctly identified"""
#         try:
#             a = AtomicComponent.objects.create(stock_code='TEST_OBJECT', quantity=1)
#             b = Blueprint.objects.create(name='TEST_BLUEPRINT')
#             br = BlueprintRequirements(required_type='Atomic', atomic_component=a, blueprint_requirement=b, quantity=1)
#             br.save()
#             self.fail("Violation of singular requirement")
#         except ValidationError:
#             pass
