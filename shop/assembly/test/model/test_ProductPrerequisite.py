from django.test import TestCase
from shop.assembly.models import ProductGroup
from shop.atomic.models import AtomicPrerequisite, AtomicSpecification, AtomicComponent
from django.core.exceptions import ValidationError

class ProductPrerequisiteTestCase(TestCase):
    def setUp(self):
        self.atom = AtomicComponent.objects.create(stock_code="ATOM", description="ATOM")

        a1 = AtomicComponent.objects.create(stock_code="ATOM1", description="ATOM1")
        a2 = AtomicComponent.objects.create(stock_code="ATOM2", description="ATOM2")



    def test_valid(self):
        prerequisite = AtomicPrerequisite.objects.create(atomic_component=self.atom, min_quantity=1, max_quantity=1)