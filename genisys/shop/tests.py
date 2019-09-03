from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import AtomicComponent, AtomicRequirement, Blueprint, BlueprintRequirement

# Create your tests here.

class AtomicComponent_create_TestCase(TestCase):
    def test(self):
        """
        Test AtomicComponent creation
        """
        try:
            a = AtomicComponent()
            a.save()
            self.fail("Violation integrity")
        except ValidationError:
            pass

class AtomicComponent_PositiveAvailability_TestCase(TestCase):
    def test(self):
        """
        Test AtomicComponent creation
        """
        a = AtomicComponent.objects.create(stock_code="LargeSupply", availability=30)
        req = AtomicRequirement.objects.create(atomic_component=a, quantity=4)
        self.assertEqual(req.available(), True)

class AtomicComponent_NegativeAvailability_TestCase(TestCase):
    def test(self):
        """
        Test AtomicComponent creation
        """
        a = AtomicComponent.objects.create(stock_code="LargeSupply", availability=3)
        req = AtomicRequirement.objects.create(atomic_component=a, quantity=40)
        self.assertEqual(req.available(), False)


class Blueprint_empty_valid_TestCase(TestCase):
    def test(self):
        """
        Test empty Blueprint
        """
        try:
            b = Blueprint(name="Table")
            b.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_assign_atomic_only_TestCase(TestCase):
    def test(self):
        """
        Test assigning 1 atomic component
        """
        a = AtomicComponent.objects.create(stock_code="TEST", part_code="Test", availability=700)
        ar = AtomicRequirement.objects.create(atomic_component=a, quantity=4)

        try:
            b = Blueprint.objects.create(name="Table")
            b.atomic_requirements.add(ar)
            b.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_assign_multiple_atomic_TestCase(TestCase):
    def test(self):
        """
        Test assign multiple atomicComponent
        """

        component = [
            AtomicComponent.objects.create(stock_code="Apple", part_code="Apple", availability=700),
            AtomicComponent.objects.create(stock_code="Orange", part_code="Orange", availability=400),
            AtomicComponent.objects.create(stock_code="Banana", part_code="Banana", availability=200)
        ]

        c_req = []
        for c in component:
            c_req.append(AtomicRequirement.objects.create(atomic_component=c, quantity=2))

        try:
            b = Blueprint.objects.create(name="Table")

            # Add all AtomicComponent requirements to Blueprint
            for req in c_req:
                b.atomic_requirements.add(req)

            b.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_assign_blueprint_TestCase(TestCase):
    def test(self):
        """
        Test assigning blueprint requirement on blueprint
        """
        try:
            a = AtomicComponent.objects.create(stock_code="TEST", part_code="Test", availability=700)
            ar = AtomicRequirement.objects.create(atomic_component=a, quantity=4)
            b = Blueprint.objects.create(name="Table")
            b.atomic_requirements.add(ar)
            b.save()

            b_set = Blueprint.objects.create(name="Table_set")
            b_set_req = BlueprintRequirement.objects.create(blueprint_component=b, quantity=2)
            b_set.blueprint_requirements.add(b_set_req)
            b_set.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_PositiveAvailability_TestCase(TestCase):

    b = Blueprint(name='Table')

    def setUp(self):
        supply = 300
        demand = 4
        r = AtomicRequirement.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.b.save()
        self.b.atomic_requirements.add(r)
        self.b.save()

    def test(self):
        self.assertEqual(self.b.available(), True)

class Blueprint_PositiveAvailability_TestCase(TestCase):

    b = Blueprint(name='Table')

    def setUp(self):
        supply = 3
        demand = 4
        r = AtomicRequirement.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.b.save()
        self.b.atomic_requirements.add(r)
        self.b.save()

    def test(self):
        self.assertEqual(self.b.available(), False)

# class Blueprint_recursive_availability_TestCase(TestCase):
#
#     tableset = Blueprint(name='Tableset')
#     table = Blueprint(name='table')
#
#     def setUp(self):
#