from django.test import TestCase
from shop.models import AtomicComponent
from .models import AtomicSpecification, Blueprint, BlueprintSpecification

class Blueprint_PositiveAvailability_SingleLayer_TestCase(TestCase):

    def setUp(self):
        supply = 300
        demand = 4

        self.b = Blueprint.objects.create(name='Table')
        r = AtomicSpecification.objects.create(
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
        r = AtomicSpecification.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.b.atomic_requirements.add(r)
        self.b.save()

    def test(self):
        self.assertEqual(self.b.available(), False)


class Blueprint_PositiveAvailability_MultiLayer_TestCase(TestCase):

    def setUp(self):
        supply = 300
        demand = 4

        self.table = Blueprint.objects.create(name='table')
        r = AtomicSpecification.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.table.atomic_requirements.add(r)
        self.table.save()
        br = BlueprintSpecification.objects.create(blueprint_component=self.table, quantity=1)

        self.tableset = Blueprint.objects.create(name='tableset')
        self.tableset.blueprint_requirements.add(br)
        self.tableset.save()

    def test(self):
        """
        Test multilayer availability
        :return:
        """
        self.assertEqual(self.tableset.available(), True)

class Blueprint_NegativeAvailability_MultiLayer_TestCase(TestCase):

    def setUp(self):
        supply = 3
        demand = 4

        self.table = Blueprint.objects.create(name='table')
        r = AtomicSpecification.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
        self.table.atomic_requirements.add(r)
        self.table.save()
        br = BlueprintSpecification.objects.create(blueprint_component=self.table, quantity=1)

        self.tableset = Blueprint.objects.create(name='tableset')
        self.tableset.blueprint_requirements.add(br)
        self.tableset.save()

    def test(self):
        """
        Test multilayer availability
        :return:
        """
        self.assertEqual(self.tableset.available(), False)