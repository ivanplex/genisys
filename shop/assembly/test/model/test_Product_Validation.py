from django.test import TestCase
from shop.assembly.models import Blueprint, ProductPrerequisite, Product, ProductSpecification
from shop.atomic.models import AtomicPrerequisite, AtomicSpecification, AtomicComponent
from django.core.exceptions import ValidationError
import re


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


class RegularAtomicSpecificationTestCase(TestCase):
    """
    Test normal product with perfectly legal specifications matching equal amount of atomic prerequisites
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
    Test Product when 1 atomic specification is missing according to its blueprint
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
        self.assertTrue('Specifications exceeded maximum limit: ATOM 2 has a maximum of 1, given 5' in context.exception)


class SegregatedAtomicSpecificationTestCase(TestCase):
    """
    Test when different Atomic Specification contribute towards same Atomic Prerequisite
    Eg. Requires 2 'ATOM_1', 2 separate specifications defined each asking for 1
    Expect no errors
    """

    def setUp(self):
        atom_1 = AtomicComponent.objects.create(stock_code="ATOM 1", description="ATOM 1")
        atom_2 = AtomicComponent.objects.create(stock_code="ATOM 2", description="ATOM 2")

        blueprint = Blueprint.objects.create(name="I'm a blueprint")
        p_atom_1 = AtomicPrerequisite.objects.create(atomic_component=atom_1, min_quantity=2, max_quantity=2)
        p_atom_2 = AtomicPrerequisite.objects.create(atomic_component=atom_2, min_quantity=1, max_quantity=1)
        blueprint.atomic_prerequisites.add(p_atom_1)
        blueprint.atomic_prerequisites.add(p_atom_2)
        blueprint.save()

        self.product = Product.objects.create(name="I'm a Product", blueprint=blueprint)
        s_atom_1_1 = AtomicSpecification.objects.create(selected_component=atom_1, prerequisite=p_atom_1, quantity=1)
        s_atom_1_2 = AtomicSpecification.objects.create(selected_component=atom_1, prerequisite=p_atom_1, quantity=1)
        s_atom_2 = AtomicSpecification.objects.create(selected_component=atom_2, prerequisite=p_atom_2, quantity=1)
        self.product.atomic_specifications.add(s_atom_1_1)
        self.product.atomic_specifications.add(s_atom_1_2)
        self.product.atomic_specifications.add(s_atom_2)
        self.product.save()

    def test(self):
        try:
            self.product.validate()
        except ValidationError:
            self.fail("False negative! 2 Atomic Specification contribute towards same prerequisite allowed!")


class RegularProductSpecificationTestCase(TestCase):
    """
    Test normal product with perfectly legal specifications matching equal amount of product prerequisites
    Expect no error
    """

    def setUp(self):
        product1 = Product.objects.create(name="PRODUCT_1", blueprint=Blueprint.objects.create(name="BLUEPRINT_1"))
        product2 = Product.objects.create(name="PRODUCT_2", blueprint=Blueprint.objects.create(name="BLUEPRINT_2"))

        blueprint = Blueprint.objects.create(name="PARENT_BLUEPRINT")
        pp_1 = ProductPrerequisite.objects.create(product=product1, min_quantity=1, max_quantity=1)
        pp_2 = ProductPrerequisite.objects.create(product=product2, min_quantity=1, max_quantity=1)
        blueprint.product_prerequisites.add(pp_1)
        blueprint.product_prerequisites.add(pp_2)
        blueprint.save()

        self.product = Product.objects.create(name="PARENT_PRODUCT", blueprint=blueprint)
        ps_1 = ProductSpecification.objects.create(selected_component=product1, prerequisite=pp_1, quantity=1)
        ps_2 = ProductSpecification.objects.create(selected_component=product2, prerequisite=pp_2, quantity=1)
        self.product.product_specifications.add(ps_1)
        self.product.product_specifications.add(ps_2)
        self.product.save()

    def test(self):
        try:
            self.product.validate()
        except ValidationError:
            self.fail("product.validate() raised ValidationError unexpectedly!")


class MissingProductSpecificationTestCase(TestCase):
    """
    Test Product when 1 product specification is missing according to its blueprint
    Expect validation error.
    """

    def setUp(self):
        product1 = Product.objects.create(name="PRODUCT_1", blueprint=Blueprint.objects.create(name="BLUEPRINT_1"))
        product2 = Product.objects.create(name="PRODUCT_2", blueprint=Blueprint.objects.create(name="BLUEPRINT_2"))

        blueprint = Blueprint.objects.create(name="PARENT_BLUEPRINT")
        pp_1 = ProductPrerequisite.objects.create(product=product1, min_quantity=1, max_quantity=1)
        pp_2 = ProductPrerequisite.objects.create(product=product2, min_quantity=1, max_quantity=1)
        blueprint.product_prerequisites.add(pp_1)
        blueprint.product_prerequisites.add(pp_2)
        blueprint.save()

        self.product = Product.objects.create(name="PARENT_PRODUCT", blueprint=blueprint)
        ps_1 = ProductSpecification.objects.create(selected_component=product1, prerequisite=pp_1, quantity=1)
        self.product.product_specifications.add(ps_1)
        self.product.save()

    def test(self):
        with self.assertRaises(ValidationError) as context:
            self.product.validate()
        r = re.compile("Insufficient specification:*")
        self.assertIsNotNone(next(filter(r.match, context.exception), None))


class ExcessiveProductSpecificationTestCase(TestCase):
    """
    Test ProductSpecifications specify a quantity over maximum
    Expected validation error
    """

    def setUp(self):
        product1 = Product.objects.create(name="PRODUCT_1", blueprint=Blueprint.objects.create(name="BLUEPRINT_1"))
        product2 = Product.objects.create(name="PRODUCT_2", blueprint=Blueprint.objects.create(name="BLUEPRINT_2"))

        blueprint = Blueprint.objects.create(name="PARENT_BLUEPRINT")
        pp_1 = ProductPrerequisite.objects.create(product=product1, min_quantity=1, max_quantity=1)
        pp_2 = ProductPrerequisite.objects.create(product=product2, min_quantity=1, max_quantity=1)
        blueprint.product_prerequisites.add(pp_1)
        blueprint.product_prerequisites.add(pp_2)
        blueprint.save()

        self.product = Product.objects.create(name="PARENT_PRODUCT", blueprint=blueprint)
        ps_1 = ProductSpecification.objects.create(selected_component=product1, prerequisite=pp_1, quantity=1)
        ps_2 = ProductSpecification.objects.create(selected_component=product2, prerequisite=pp_2, quantity=5)
        self.product.product_specifications.add(ps_1)
        self.product.product_specifications.add(ps_2)
        self.product.save()

    def test(self):
        with self.assertRaises(ValidationError) as context:
            self.product.validate()
        r = re.compile("Specifications exceeded maximum limit:*")
        self.assertIsNotNone(next(filter(r.match, context.exception), None))


class SegregatedProductSpecificationTestCase(TestCase):
    """
    Test when different Product Specification contribute towards same Product Prerequisite
    Eg. Requires 2 'PRODUCT_1', 2 separate specifications defined each asking for 1
    Expect no errors
    """

    def setUp(self):
        product1 = Product.objects.create(name="PRODUCT_1", blueprint=Blueprint.objects.create(name="BLUEPRINT_1"))
        product2 = Product.objects.create(name="PRODUCT_2", blueprint=Blueprint.objects.create(name="BLUEPRINT_2"))

        blueprint = Blueprint.objects.create(name="PARENT_BLUEPRINT")
        pp_1 = ProductPrerequisite.objects.create(product=product1, min_quantity=2, max_quantity=2)
        pp_2 = ProductPrerequisite.objects.create(product=product2, min_quantity=1, max_quantity=1)
        blueprint.product_prerequisites.add(pp_1)
        blueprint.product_prerequisites.add(pp_2)
        blueprint.save()

        self.product = Product.objects.create(name="PARENT_PRODUCT", blueprint=blueprint)
        ps_1_1 = ProductSpecification.objects.create(selected_component=product1, prerequisite=pp_1, quantity=1)
        ps_1_2 = ProductSpecification.objects.create(selected_component=product1, prerequisite=pp_1, quantity=1)
        ps_2 = ProductSpecification.objects.create(selected_component=product2, prerequisite=pp_2, quantity=1)
        self.product.product_specifications.add(ps_1_1)
        self.product.product_specifications.add(ps_1_2)
        self.product.product_specifications.add(ps_2)
        self.product.save()

    def test(self):
        try:
            self.product.validate()
        except ValidationError:
            self.fail("False negative! 2 Product Specification contribute towards same prerequisite allowed!")
