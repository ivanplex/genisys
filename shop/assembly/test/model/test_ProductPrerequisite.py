from django.test import TestCase
from shop.assembly.models import Blueprint, Product, ProductGroup, ProductPrerequisite
from django.core.exceptions import ValidationError


class ProductPrerequisiteTestCase(TestCase):
    """
    Test case for ProductPrerequisite. Ensure product and product_group
    cannot be empty at the same time
    """
    def setUp(self):
        blueprint = Blueprint.objects.create(name="BLUEPRINT")
        self.product = Product.objects.create(name="PRODUCT", blueprint=blueprint)

        product1 = Product.objects.create(name="PRODUCT", blueprint=blueprint)
        product2 = Product.objects.create(name="PRODUCT", blueprint=blueprint)

        self.group = ProductGroup.objects.create(name="PRODUCT_GROUP")
        self.group.members.add(product1)
        self.group.members.add(product2)
        self.group.save()

    def test_valid_component_only(self):
        prerequisite = ProductPrerequisite(min_quantity=1, max_quantity=1)
        prerequisite.product = self.product
        try:
            prerequisite.save()
        except ValidationError:
            self.fail("ProductPrerequisite raised ValidationError unexpectedly!")

    def test_valid_group_only(self):
        prerequisite = ProductPrerequisite(min_quantity=1, max_quantity=1)
        prerequisite.product_group = self.group
        try:
            prerequisite.save()
        except ValidationError:
            self.fail("ProductPrerequisite raised ValidationError unexpectedly!")

    def test_valid_component_and_group(self):
        prerequisite = ProductPrerequisite(min_quantity=1, max_quantity=1)
        prerequisite.product = self.product
        prerequisite.product_group = self.group
        try:
            prerequisite.save()
        except ValidationError:
            self.fail("ProductPrerequisite raised ValidationError unexpectedly!")

    def test_invalid(self):
        """
        both empty
        :return: ValidationError
        """
        prerequisite = ProductPrerequisite(min_quantity=1, max_quantity=1)
        with self.assertRaises(ValidationError) as context:
            prerequisite.save()
        self.assertTrue('ProductPrerequisite has no assigned product or product-group' in context.exception)
