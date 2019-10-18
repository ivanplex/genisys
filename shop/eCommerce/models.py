from django.db import models
from shop.models import TimestampedModel

class ECOMProductImage(TimestampedModel):
    image_link = models.URLField(null=False)

class ECOMProduct(TimestampedModel):

    YES_NO = [
        'yes',
        'no',
    ]

    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(null=False)
    image_link = models.ForeignKey(ECOMProductImage, on_delete=models.CASCADE,
                                   related_name='image_link', null=False)
    additional_image_link = models.ManyToManyField(ECOMProductImage, related_name='additional_image_link',
                                                   symmetrical=False)
    mobile_link = models.URLField(blank=True, null=True)

    AVAILABILITY_CHOICE = [
        'in stock',
        'out of stock',
        'preorder',
    ]
    availability = models.CharField(choices=AVAILABILITY_CHOICE, null=False)
    availability_date = models.DateTimeField(max_length=25, format='%Y-%m-%d %H:%M:%S')
    cost_of_goods_sold = models.FloatField()
    expiration_date = models.DateTimeField(max_length=25, format='%Y-%m-%d %H:%M:%S')
    price = models.FloatField(null=False)
    sale_price = models.FloatField(null=False)
    sale_price_effective_date = models.DateTimeField(max_length=25, format='%Y-%m-%d %H:%M:%S')
    unit_pricing_measure = models.CharField(max_length=255)
    unit_pricing_base_measure = models.CharField(max_length=255)
    installment = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)
    loyalty_points = models.CharField(max_length=255)
    google_product_category = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    brand = models.CharField(max_length=70, null=False)
    gtin = models.CharField(max_length=255)
    MPN = models.CharField(max_length=70, null=True)
    identifier_exists = models.CharField(max_length=3, choices=YES_NO)
    CONDITIONS = [
        ('new', 'NewCondition'),
        ('refurbished', 'RefurbishedCondition'),
        ('used', 'UsedCondition'),
    ]
    condition = models.CharField(max_length=255, null=True, choices=CONDITIONS)
    adult = models.CharField(max_length=3, choices=YES_NO)
    multipack = models.CharField(max_length=255, null=True)
    is_bundle = models.CharField(max_length=3, choices=YES_NO)
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
    age_group = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=100, null=False)
    GENDER_CHOICES = [
        'male',
        'female',
        'unisex',
    ]
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    material = models.CharField(max_length=200, null=False)
    pattern = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=100, null=False)
    size_type = models.CharField(max_length=100, null=True, blank=True)
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
    adwords_redirect = models.URLField(max_length=2000)
    custom_label_0 = models.CharField(max_length=100, null=True, blank=True)
    promotion_id = models.CharField(max_length=50, null=True, blank=True)
    excluded_destination = models.CharField(max_length=255, null=True, blank=True)
    included_destination = models.CharField(max_length=255, null=True, blank=True)



    def save(self, *args, **kwargs):
        # Format currency to 2dp
        self.cost_of_goods_sold = round(self.cost_of_goods_sold, 2)
        self.price = round(self.price, 2)
        self.sale_price = round(self.sale_price, 2)
        super(ECOMProduct, self).save(*args, **kwargs)
