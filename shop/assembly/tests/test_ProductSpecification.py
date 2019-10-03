from django.test import TestCase
from shop.atomic.models import AtomicComponent, AtomicSpecification, AtomicPrerequisite
from shop.assembly.models import Blueprint, Product


class ProductSpecificationValidationTestCase(TestCase):

    def setUp(self):
        minimum = 4
        maximum = 8
        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prerequisite = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=minimum, max_quantity=maximum)
        self.blueprint.atomic_prerequisites.add(self.atomic_prerequisite)
        self.blueprint.save()

    def test_winthin_bound(self):
        """
        BuildSpecification following product prerequisite
        """
        spec_quantity = 6

        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)
        self.spec = AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite, quantity=spec_quantity)
        self.product.atomic_specifications.add(self.spec)
        self.product.save()

        self.assertTrue(self.product.validate_spec())

    def test_out_of_bound(self):
        """
        BuildSpecification NOT following product prerequisite
        """
        spec_quantity = 20

        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)
        self.spec = AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite, quantity=spec_quantity)
        self.product.atomic_specifications.add(self.spec)
        self.product.save()

        self.assertFalse(self.product.validate_spec())


class MultipleProductSpecificationValidationTestCase(TestCase):

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
                atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
                min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
                atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
                min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)

    def test_within_bound(self):
        """
        All BuildSpecification following product prerequisite
        """
        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=6)
        ]
        for spec in self.atomic_specs:
            self.product.atomic_specifications.add(spec)
        self.product.save()
        self.assertTrue(self.product.validate_spec())

    def test_out_of_bound(self):
        """
        1 of the BuildSpecification NOT following product prerequisite
        """
        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=20)
        ]
        for spec in self.atomic_specs:
            self.product.atomic_specifications.add(spec)
        self.product.save()
        self.assertFalse(self.product.validate_spec())
