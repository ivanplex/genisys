from django.test import TestCase
from shop.assembly.models import Blueprint, ProductPrerequisite, Product, ProductSpecification
from shop.atomic.models import AtomicPrerequisite, AtomicSpecification, AtomicComponent
from django.core.exceptions import ValidationError


class RegularTestCase(TestCase):
    """
    Test normal product with perfectly legal specifications matching equal amount of prerequisites
    Expect no error
    """

    def setUp(self):
        atom_1 = AtomicComponent.objects.create(stock_code="ATOM 1", description="ATOM 1")
        atom_2 = AtomicComponent.objects.create(stock_code="ATOM 2", description="ATOM 2")

        blueprint = Blueprint.objects.create(name="I'm a blueprint")
        p_atom_1 = AtomicPrerequisite.objects.create(atomic_component=atom_1, min_quantity=1, max_quantity=1)
        p_atom_2 = AtomicPrerequisite.objects.create(atomic_component=atom_2, min_quantity=1, max_quantity=1)
        blueprint.atomic_prerequisites.add(p_atom_1)
        blueprint.atomic_prerequisites.add(p_atom_2)
        blueprint.save()

        self.product = Product.objects.create(name="I'm a Product", blueprint=blueprint)
        s_atom_1 = AtomicSpecification.objects.create(selected_component=atom_1, prerequisite=p_atom_1, quantity=1)
        s_atom_2 = AtomicSpecification.objects.create(selected_component=atom_2, prerequisite=p_atom_2, quantity=1)
        self.product.atomic_specifications.add(s_atom_1)
        self.product.atomic_specifications.add(s_atom_2)
        self.product.save()

    def test(self):
        try:
            self.product.validate()
        except ValidationError:
            self.fail("product.validate() raised ValidationError unexpectedly!")


class MissingAtomicSpecificationTestCase(TestCase):
    """
    Test Product when 1 specification is missing according to its blueprint
    Expect validation error.
    """

    def setUp(self):
        atom_1 = AtomicComponent.objects.create(stock_code="ATOM 1", description="ATOM 1")
        atom_2 = AtomicComponent.objects.create(stock_code="ATOM 2", description="ATOM 2")

        blueprint = Blueprint.objects.create(name="I'm a blueprint")
        p_atom_1 = AtomicPrerequisite.objects.create(atomic_component=atom_1, min_quantity=1, max_quantity=1)
        p_atom_2 = AtomicPrerequisite.objects.create(atomic_component=atom_2, min_quantity=1, max_quantity=1)
        blueprint.atomic_prerequisites.add(p_atom_1)
        blueprint.atomic_prerequisites.add(p_atom_2)
        blueprint.save()

        self.product = Product.objects.create(name="I'm a Product", blueprint=blueprint)
        s_atom_1 = AtomicSpecification.objects.create(selected_component=atom_1, prerequisite=p_atom_1, quantity=1)
        self.product.atomic_specifications.add(s_atom_1)
        self.product.save()

    def test(self):
        with self.assertRaises(ValidationError) as context:
            self.product.validate()
        self.assertTrue('Insufficient specification: ATOM 2 requires minimum of 1, given 0' in context.exception)


class ExcessiveAtomicSpecificationTestCase(TestCase):
    """
    Test AtomicSpecifications specify a quantity over maximum
    Expected validation error
    """

    def setUp(self):
        atom_1 = AtomicComponent.objects.create(stock_code="ATOM 1", description="ATOM 1")
        atom_2 = AtomicComponent.objects.create(stock_code="ATOM 2", description="ATOM 2")

        blueprint = Blueprint.objects.create(name="I'm a blueprint")
        p_atom_1 = AtomicPrerequisite.objects.create(atomic_component=atom_1, min_quantity=1, max_quantity=1)
        p_atom_2 = AtomicPrerequisite.objects.create(atomic_component=atom_2, min_quantity=1, max_quantity=1)
        blueprint.atomic_prerequisites.add(p_atom_1)
        blueprint.atomic_prerequisites.add(p_atom_2)
        blueprint.save()

        self.product = Product.objects.create(name="I'm a Product", blueprint=blueprint)
        s_atom_1 = AtomicSpecification.objects.create(selected_component=atom_1, prerequisite=p_atom_1, quantity=1)
        # required exactly 1, given 5
        s_atom_2 = AtomicSpecification.objects.create(selected_component=atom_2, prerequisite=p_atom_2, quantity=5)
        self.product.atomic_specifications.add(s_atom_1)
        self.product.atomic_specifications.add(s_atom_2)
        self.product.save()

    def test(self):
        with self.assertRaises(ValidationError) as context:
            self.product.validate()
        self.assertTrue('Specifications exceeded maximum limit: ATOM 2 has a maximum of 1, given 2' in context.exception)


class EmptyBlueprintValidationTestCase(TestCase):
    """
    Test empty blueprint. 0 prerequisite vs 0 specification.
    This is a valid call. Expect no error.
    """

    def setUp(self):
        blueprint = Blueprint.objects.create(name="I'm a blueprint")
        self.product = Product.objects.create(name="I'm a Product", blueprint=blueprint)

    def test(self):
        try:
            self.product.validate()
        except ValidationError:
            self.fail("product.validate() raised ValidationError unexpectedly!")


class EmptyAtomicSpecificationTestCase(TestCase):
    """
    Test regular Blueprint with 2 prerequisite, but product has no specification pointing
    to any prerequisites
    Expect validation error.
    """

    def setUp(self):
        atom_1 = AtomicComponent.objects.create(stock_code="ATOM 1", description="ATOM 1")
        atom_2 = AtomicComponent.objects.create(stock_code="ATOM 2", description="ATOM 2")

        blueprint = Blueprint.objects.create(name="I'm a blueprint")
        p_atom_1 = AtomicPrerequisite.objects.create(atomic_component=atom_1, min_quantity=1, max_quantity=1)
        p_atom_2 = AtomicPrerequisite.objects.create(atomic_component=atom_2, min_quantity=1, max_quantity=1)
        blueprint.atomic_prerequisites.add(p_atom_1)
        blueprint.atomic_prerequisites.add(p_atom_2)
        blueprint.save()

        self.product = Product.objects.create(name="I'm a Product", blueprint=blueprint)

    def test(self):
        with self.assertRaises(ValidationError) as context:
            self.product.validate()
        self.assertTrue('Insufficient specification: ATOM 1 requires minimum of 1, given 0' in context.exception)
