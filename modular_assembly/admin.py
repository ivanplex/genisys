from django.contrib import admin

from modular_assembly.atomic.models import AtomicComponent, AtomicSpecification, AtomicPrerequisite
from modular_assembly.assembly.models import Blueprint, Product, ProductSpecification, ProductPrerequisite
from modular_assembly.eCommerce.models import ECOMProductImage, ECOMProduct

admin.site.register(AtomicComponent)
admin.site.register(AtomicPrerequisite)
admin.site.register(AtomicSpecification)
admin.site.register(Blueprint)
admin.site.register(Product)
admin.site.register(ProductSpecification)
admin.site.register(ProductPrerequisite)
admin.site.register(ECOMProduct)
admin.site.register(ECOMProductImage)

