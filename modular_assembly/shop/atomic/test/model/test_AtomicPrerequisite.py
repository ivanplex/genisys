from django.test import TestCase
from shop.atomic.models import AtomicPrerequisite, AtomicComponent, AtomicGroup
from django.core.exceptions import ValidationError


class AtomicPrerequisiteTestCase(TestCase):
    """
    Test case for AtomicPrerequisite. Ensure atomic_component and atomic_group
    cannot be empty at the same time
    """
    def setUp(self):
        self.atom = AtomicComponent.objects.create(sku="ATOM", description="ATOM")

        a1 = AtomicComponent.objects.create(sku="ATOM1", description="ATOM1")
        a2 = AtomicComponent.objects.create(sku="ATOM2", description="ATOM2")
        self.group = AtomicGroup.objects.create(name="ATOM GROUP")
        self.group.members.add(a1)
        self.group.members.add(a2)
        self.group.save()

    def test_valid_component_only(self):
        prerequisite = AtomicPrerequisite(min_quantity=1, max_quantity=1)
        prerequisite.atomic_component = self.atom
        try:
            prerequisite.save()
        except ValidationError:
            self.fail("AtomicPrerequisite raised ValidationError unexpectedly!")

    def test_valid_group_only(self):
        prerequisite = AtomicPrerequisite(min_quantity=1, max_quantity=1)
        prerequisite.atomic_group = self.group
        try:
            prerequisite.save()
        except ValidationError:
            self.fail("AtomicPrerequisite raised ValidationError unexpectedly!")

    def test_valid_component_and_group(self):
        prerequisite = AtomicPrerequisite(min_quantity=1, max_quantity=1)
        prerequisite.atomic_component = self.atom
        prerequisite.atomic_group = self.group
        try:
            prerequisite.save()
        except ValidationError:
            self.fail("AtomicPrerequisite raised ValidationError unexpectedly!")

    def test_invalid(self):
        """
        both empty
        :return: ValidationError
        """
        prerequisite = AtomicPrerequisite(min_quantity=1, max_quantity=1)
        with self.assertRaises(ValidationError) as context:
            prerequisite.save()
        self.assertTrue('AtomicPrerequisite has no assigned product or atomic-group' in context.exception)
