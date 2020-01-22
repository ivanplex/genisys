from django.contrib import admin

from shop.atomic.models import AtomicComponent, AtomicSpecification, AtomicPrerequisite
from shop.assembly.models import Blueprint, Product, ProductSpecification, ProductPrerequisite
from shop.eCommerce.models import ECOMProductImage, ECOMProduct

admin.site.register(AtomicComponent)
admin.site.register(AtomicPrerequisite)
admin.site.register(AtomicSpecification)
admin.site.register(Blueprint)
admin.site.register(Product)
admin.site.register(ProductSpecification)
admin.site.register(ProductPrerequisite)
admin.site.register(ECOMProduct)
admin.site.register(ECOMProductImage)

