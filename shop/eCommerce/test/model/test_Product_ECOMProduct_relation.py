from django.test import TestCase
from shop.eCommerce.models import ECOMProduct, ECOMProductImage
from shop.assembly.models import Product, Blueprint


class RelationTestCase(TestCase):
    """
    Test model cascade relation
    If Product is removed, ECOMProduct should also be removed
    """
    def setUp(self):
        blueprint = Blueprint.objects.create(name='BLUEPRINT')
        self.product = Product.objects.create(name='PRODUCT', blueprint=blueprint)
        self.ecom_product = ECOMProduct.objects.create(product=self.product,
                                                       title='ECOM-PRODUCT',
                                                       description='Test E-commerce Product',
                                                       image_link=ECOMProductImage.objects.create(
                                                           image_link='https://images.google.com/'),
                                                       availability='in stock',
                                                       price=21.12,
                                                       brand='Alrose',
                                                       gtin='1234567890',
                                                       condition='new',
                                                       adult='no',
                                                       is_bundle='no',
                                                       material='',
                                                       pattern='',
                                                       item_group_id='1',
                                                       shipping='n/a',
                                                       tax='n/a'
                                   )

    def test(self):
        self.product.delete()
        self.assertFalse(ECOMProduct.objects.filter(
            title='ECOM-PRODUCT').exists())
