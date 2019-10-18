from django.db import models
from shop.models import TimestampedModel


class ECOMProductImage(TimestampedModel):
    image_link = models.URLField(null=False)


class ECOMProduct(TimestampedModel):

    YES_NO = [
        'yes',
        'no',
    ]

    title = models.CharField(max_length=150, null=False)
    description = models.TextField(blank=True, null=False)
    link = models.URLField(null=False)
    image_link = models.ForeignKey(ECOMProductImage, on_delete=models.CASCADE,
                                   related_name='image_link', null=False)
    additional_image_link = models.ManyToManyField(ECOMProductImage, related_name='additional_image_link',
                                                   symmetrical=False, blank=True)
    mobile_link = models.URLField(blank=True, null=True)

    AVAILABILITY_CHOICE = [
        'in stock',
        'out of stock',
        'preorder',
    ]
    availability = models.CharField(choices=AVAILABILITY_CHOICE, null=False)
    availability_date = models.DateTimeField(max_length=25, format='%Y-%m-%d %H:%M:%S')
    cost_of_goods_sold = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    expiration_date = models.DateTimeField(max_length=25, format='%Y-%m-%d %H:%M:%S')
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sale_price_effective_date = models.DateTimeField(max_length=25, format='%Y-%m-%d %H:%M:%S')
    unit_pricing_measure = models.CharField(max_length=255, null=True, blank=True)
    unit_pricing_base_measure = models.CharField(max_length=255, null=True, blank=True)
    installment = models.CharField(max_length=255, null=True, blank=True)
    subscription_cost = models.CharField(max_length=255, null=True, blank=True)
    loyalty_points = models.CharField(max_length=255, null=True, blank=True)
    google_product_category = models.CharField(max_length=255, null=True, blank=True)
    product_type = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=70, null=False)
    gtin = models.CharField(max_length=255, null=False)
    MPN = models.CharField(max_length=70, null=True, blank=True)
    identifier_exists = models.CharField(max_length=3, choices=YES_NO)
    CONDITIONS = [
        ('new', 'NewCondition'),
        ('refurbished', 'RefurbishedCondition'),
        ('used', 'UsedCondition'),
    ]
    condition = models.CharField(max_length=255, null=False, choices=CONDITIONS)
    adult = models.CharField(max_length=3, choices=YES_NO, null=False)
    multipack = models.CharField(max_length=255, null=False)
    is_bundle = models.CharField(max_length=3, choices=YES_NO, null=False)
    ENERGY_EFFICIENCY = [
        'A+++',
        'A++'
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
    ]
    energy_efficiency_class = models.CharField(max_length=255, choices=ENERGY_EFFICIENCY)
    min_energy_efficiency_class = models.CharField(max_length=255, choices=ENERGY_EFFICIENCY)
    max_energy_efficiency_class = models.CharField(max_length=255, choices=ENERGY_EFFICIENCY)
    AGE_GROUP_CHOICE = [
        ('newborn', 'Up to 3 months old'),
        ('infant', '3-12 months old'),
        ('toddler', '1-5 years old'),
        ('kids', '5-13 years old'),
        ('adult', 'Older than 13')
    ]
    age_group = models.CharField(max_length=255, choices=AGE_GROUP_CHOICE, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    GENDER_CHOICES = [
        'male',
        'female',
        'unisex',
    ]
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    material = models.CharField(max_length=200, null=False)
    pattern = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=100, null=True, blank=True)
    SIZE_TYPE = [
        ('regular', 'Regular'),
        ('petite', 'Petite'),
        ('plus', 'Plus'),
        ('big and tall', 'Big and Tall'),
        ('maternity', 'Maternity'),
    ]
    size_type = models.CharField(max_length=100, choice=SIZE_TYPE, null=True, blank=True)
    SIZE_SYSTEM_CHOICES = [
        'US',
        'UK',
        'EU',
        'DE',
        'FR',
        'JP',
        'CN (CHINA)',
        'IT',
        'BR',
        'MEX',
        'AU',
    ]
    size_system = models.CharField(max_length=255, choices=GENDER_CHOICES)
    item_group_id = models.CharField(max_length=50, null=False)
    adwords_redirect = models.URLField(max_length=2000, null=True, blank=True)
    custom_label_0 = models.CharField(max_length=100, null=True, blank=True)
    promotion_id = models.CharField(max_length=50, null=True, blank=True)
    ADVERTISING_DESTINATIONS = [
        'Shopping Ads',
        'Shopping Actions',
        'Display Ads',
        'Surface across Google',
    ]
    excluded_destination = models.CharField(max_length=255, choices=ADVERTISING_DESTINATIONS, null=True, blank=True)
    included_destination = models.CharField(max_length=255, choices=ADVERTISING_DESTINATIONS, null=True, blank=True)
    shipping = models.CharField(max_length=255, null=False)
    shipping_label = models.CharField(max_length=100, null=True, blank=True)
    shipping_weight = models.CharField(max_length=255, null=True, blank=True)
    delivery_length = models.CharField(max_length=255, null=True, blank=True)
    shipping_width = models.CharField(max_length=255, null=True, blank=True)
    shipping_height = models.CharField(max_length=255, null=True, blank=True)
    transit_time_label = models.CharField(max_length=100, null=True, blank=True)
    max_handling_time = models.CharField(max_length=255, null=True, blank=True)
    min_handling_time = models.IntegerField()
    tax = models.CharField(max_length=255, null=False)
    tax_category = models.CharField(max_length=100, null=True, blank=True)
