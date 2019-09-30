from django.test import TestCase

class GroupClassTestCase(TestCase):
    def setUp(self):
        atom = AtomicComponent.objects.create(
            stock_code="p_bolt",
            part_code="p_bolt",
            description="General purpose Philip bolt",
            warehouse_location="2000",
            material="",
            weight=3,
            image="/img/bolt.png",
            availability=6000,
        )