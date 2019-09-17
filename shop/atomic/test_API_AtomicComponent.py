from rest_framework.test import APITestCase

from shop.atomic.models import AtomicComponent
from shop.atomic.serializers import AtomicComponentSerializer


class AtomicComponentTests(APITestCase):
    def test_can_get_product_details(self):
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
        response = self.client.get(f'/atomic/component/view/{atom.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, AtomicComponentSerializer(instance=atom).data)

    def test_can_delete_product(self):
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
        response = self.client.delete(f'/atomic/component/delete/{atom.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(AtomicComponent.objects.count(), 0)

    def test_can_update_product(self):
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
        response = self.client.patch(f'/atomic/component/update/{atom.id}/', data={'material': 'Steel'})
        atom.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(atom.material, 'Steel')
