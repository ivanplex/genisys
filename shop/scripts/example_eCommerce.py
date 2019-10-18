from shop.eCommerce.models import ECOMProduct, ECOMProductImage
from shop.assembly.models import Product, Blueprint


def run():
    blueprint = Blueprint.objects.create(name="Example blueprint for eCommerce Product")
    product = Product.objects.create(name="Example product for eCommerce product", blueprint=blueprint)

    print("     Creating eProduct - Woo Logo")
    p1 = ECOMProduct.objects.create(product=product,
                               title='Woo Logo',
                               description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.',
                               image_link=ECOMProductImage.objects.create(
                                   image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_1_front.jpg'),
                               availability='in stock',
                               price=43.77,
                               brand='SuperWet',
                               gtin='235345324',
                               condition='new',
                               adult='no',
                               multipack=1,
                               is_bundle='no',
                               material='cotton',
                               pattern='checks',
                               size='M',
                               item_group_id='1',
                               shipping='5',
                               tax='20'
                               )
    p1.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_5_front.jpg'))
    p1.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_5_back.jpg'))
    p1.save()

    print("     Creating eProduct - Ninja Silhouette")
    p2 = ECOMProduct.objects.create(product=product,
                                    title='Ninja Silhouette',
                                    description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.',
                                    image_link=ECOMProductImage.objects.create(
                                        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_7_front.jpg'),
                                    availability='in stock',
                                    price=75.99,
                                    brand='Niike',
                                    gtin='43534523',
                                    condition='new',
                                    adult='no',
                                    multipack=1,
                                    is_bundle='no',
                                    material='wool',
                                    pattern='dots',
                                    item_group_id='1',
                                    shipping='5',
                                    tax='20'
                                    )
    p2.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_4_front.jpg'))
    p2.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_4_back.jpg'))
    p2.save()

    print("     Creating eProduct - Happy Ninja")
    p3 = ECOMProduct.objects.create(product=product,
                                    title='Happy Ninja',
                                    description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.',
                                    image_link=ECOMProductImage.objects.create(
                                        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_3_front.jpg'),
                                    availability='in stock',
                                    price=106.23,
                                    brand='SuperWet',
                                    gtin='45234rt',
                                    condition='new',
                                    adult='no',
                                    multipack=1,
                                    is_bundle='no',
                                    material='poly',
                                    pattern='squares',
                                    item_group_id='1',
                                    shipping='5',
                                    tax='20'
                                    )
    p3.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_3_front.jpg'))
    p3.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_3_back.jpg'))
    p3.save()

    print("     Creating eProduct - Patient Ninja")
    p4 = ECOMProduct.objects.create(product=product,
                                    title='Patient Ninja',
                                    description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.',
                                    image_link=ECOMProductImage.objects.create(
                                        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_4_front1.jpg'),
                                    availability='in stock',
                                    price=137.46,
                                    brand='Niike',
                                    gtin='vgfgh675676',
                                    condition='new',
                                    adult='no',
                                    multipack=1,
                                    is_bundle='no',
                                    material='ss',
                                    pattern='none',
                                    item_group_id='1',
                                    shipping='5',
                                    tax='20'
                                    )
    p4.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_2_front.jpg'))
    p4.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_2_back.jpg'))
    p4.save()

    print("     Creating eProduct - Woo Ninja")
    p5 = ECOMProduct.objects.create(product=product,
                                    title='Woo Ninja',
                                    description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.',
                                    image_link=ECOMProductImage.objects.create(
                                        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/cd_5_angle.jpg'),
                                    availability='in stock',
                                    price=168.69,
                                    brand='SuperWet',
                                    gtin='54866537',
                                    condition='new',
                                    adult='no',
                                    multipack=1,
                                    is_bundle='no',
                                    material='cotton',
                                    pattern='waves',
                                    item_group_id='1',
                                    shipping='5',
                                    tax='20'
                                    )
    p5.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_1_front.jpg'))
    p5.additional_image_link.add(ECOMProductImage.objects.create(
        image_link='http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/hoodie_1_back.jpg'))
    p5.save()

    print("Import finished.")
    print()
