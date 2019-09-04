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

class Blueprint_TrueEmpty_TestCase(TestCase):

    def setUp(self):
        self.table = Blueprint.objects.create(name='table')

    def test(self):
        """
        True empty of a Blueprint
        """
        self.assertEqual(self.table.isEmpty(), True)


class Blueprint_FalseEmpty_1_TestCase(TestCase):

    def setUp(self):
        self.table = Blueprint.objects.create(name='table')
        r = AtomicRequirement.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300), quantity=12)
        self.table.atomic_requirements.add(r)
        self.table.save()

    def test(self):
        """
        False empty when blueprint contains atomicComponent
        """
        self.assertEqual(self.table.isEmpty(), False)

class Blueprint_FalseEmpty_2_TestCase(TestCase):

    def setUp(self):
        self.tableset = Blueprint.objects.create(name='tableset')
        self.table = Blueprint.objects.create(name='table')
        r = AtomicRequirement.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300), quantity=12)
        self.table.atomic_requirements.add(r)
        self.table.save()
        br = BlueprintRequirement.objects.create(blueprint_component=self.table, quantity=1)

        self.tableset.blueprint_requirements.add(br)
        self.tableset.save()

    def test(self):
        """
        False empty when blueprint contains blueprint
        """
        self.assertEqual(self.tableset.isEmpty(), False)

class Blueprint_FalseEmpty_3_TestCase(TestCase):

    def setUp(self):
        self.tableset = Blueprint.objects.create(name='tableset')
        self.table = Blueprint.objects.create(name='table')
        r1 = AtomicRequirement.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300), quantity=12)
        r2 = AtomicRequirement.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300), quantity=12)
        self.table.atomic_requirements.add(r1)
        self.table.save()
        br = BlueprintRequirement.objects.create(blueprint_component=self.table, quantity=1)

        self.tableset.blueprint_requirements.add(br)
        self.tableset.atomic_requirements.add(r2)
        self.tableset.save()

    def test(self):
        """
        False empty when blueprint contains both blueprint and atomic
        """
        self.assertEqual(self.tableset.isEmpty(), False)

class Blueprint_PositiveAvailability_SingleLayer_TestCase(TestCase):

    def setUp(self):
        supply = 300
        demand = 4

        self.b = Blueprint.objects.create(name='Table')
        r = AtomicRequirement.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.b.atomic_requirements.add(r)
        self.b.save()

    def test(self):
        self.assertEqual(self.b.available(), True)

class Blueprint_NegativeAvailability_SingleLayer_TestCase(TestCase):

    def setUp(self):
        supply = 3
        demand = 4

        self.b = Blueprint.objects.create(name='Table')
        r = AtomicRequirement.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.b.atomic_requirements.add(r)
        self.b.save()

    def test(self):
        self.assertEqual(self.b.available(), False)

class Blueprint_recursive_availability_TestCase(TestCase):
    """
    Recursive test case.

    Scenario: Ikea table set

    Table-set contains 1 table (blueprint) and 4 chairs (blueprint)
    and a instruction manual (atomic)

    A table contains 1 table-top, 4 legs, 4 screws
    A chair contains a backplate and 4 legs, 4 screws
    """

    def setUp(self):

        self.manual = AtomicComponent.objects.create(stock_code="man", availability=5)
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)
        self.backplate = AtomicComponent.objects.create(stock_code="backplate", availability=15)

        # Table
        tableRequirements = [
            AtomicRequirement.objects.create(atomic_component=self.tabletop, quantity=1),
            AtomicRequirement.objects.create(atomic_component=self.leg, quantity=4),
            AtomicRequirement.objects.create(atomic_component=self.screws, quantity=4)
        ]
        self.tableBlueprint = Blueprint.objects.create(name="table")
        for req in tableRequirements:
            self.tableBlueprint.atomic_requirements.add(req)
        self.tableBlueprint.save()

        # Chair
        chairRequirements = [
            AtomicRequirement.objects.create(atomic_component=self.backplate, quantity=1),
            AtomicRequirement.objects.create(atomic_component=self.leg, quantity=4),
            AtomicRequirement.objects.create(atomic_component=self.screws, quantity=4)
        ]
        self.chairBlueprint = Blueprint.objects.create(name="chair")
        for req in chairRequirements:
            self.chairBlueprint.atomic_requirements.add(req)
        self.chairBlueprint.save()

        # Table set
        self.tableset = Blueprint.objects.create(name="tableset")
        tablesetAtomicRequirement = AtomicRequirement.objects.create(atomic_component=self.manual, quantity=1)
        tablesetBlueprintRequirement = [
            BlueprintRequirement.objects.create(blueprint_component=self.tableBlueprint, quantity=1),
            BlueprintRequirement.objects.create(blueprint_component=self.chairBlueprint, quantity=4)
        ]
        self.tableset.atomic_requirements.add(tablesetAtomicRequirement)
        for bpReq in tablesetBlueprintRequirement:
            self.tableset.blueprint_requirements.add(bpReq)
        self.tableset.save()

        # create a list of all requirements
        self.allAtomicRequirements = tableRequirements + chairRequirements + [tablesetAtomicRequirement]

    def test(self):
        self.assertEqual(set(self.tableset.listAtomicDependencies()), set(self.allAtomicRequirements))


class Blueprint_PositiveAvailability_MultiLayer_TestCase(TestCase):

    def setUp(self):
        supply = 300
        demand = 4

        self.table = Blueprint.objects.create(name='table')
        r = AtomicRequirement.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.table.atomic_requirements.add(r)
        self.table.save()
        br = BlueprintRequirement.objects.create(blueprint_component=self.table, quantity=1)

        self.tableset = Blueprint.objects.create(name='tableset')
        self.tableset.blueprint_requirements.add(br)
        self.tableset.save()

    def test(self):
        self.assertEqual(self.tableset.available(), True)

class Blueprint_PositiveAvailability_MultiLayer_TestCase(TestCase):

    def setUp(self):
        supply = 3
        demand = 4

        self.table = Blueprint.objects.create(name='table')
        r = AtomicRequirement.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.table.atomic_requirements.add(r)
        self.table.save()
        br = BlueprintRequirement.objects.create(blueprint_component=self.table, quantity=1)

        self.tableset = Blueprint.objects.create(name='tableset')
        self.tableset.blueprint_requirements.add(br)
        self.tableset.save()

    def test(self):
        self.assertEqual(self.tableset.available(), False)
