from django.test import TestCase
from modular_assembly.atomic.models import AtomicComponent, AtomicGroup


class GroupClassTestCase(TestCase):
    def setUp(self):
        self.atom1 = AtomicComponent.objects.create(
            sku="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        self.atom2 = AtomicComponent.objects.create(
            sku="s_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )
        self.atom3 = AtomicComponent.objects.create(
            sku="t_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )

    def test_adding(self):
        g = AtomicGroup.objects.create(name="bolt")
        g.members.add(self.atom1)
        g.members.add(self.atom2)
        g.members.add(self.atom3)
        g.save()

        self.assertEqual(len(g.members.all()), 3)

    def test_remove(self):
        g = AtomicGroup.objects.create(name="bolt")
        g.members.add(self.atom1)
        g.members.add(self.atom2)
        g.members.add(self.atom3)
        g.save()

        self.atom3.delete()

        self.assertEqual(len(g.members.all()), 2)

