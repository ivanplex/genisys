from django.db import models
from shop.models import TimestampedModel, URL, OffsetImageURL
from shop.relations.models import Prerequisite, Specification
from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification
from shop.attribute.models import Attribute
from shop.group.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Blueprint(TimestampedModel):
    name = models.CharField(max_length=250, unique=True)
    atomic_prerequisites = models.ManyToManyField(AtomicPrerequisite, related_name='atomic_requirements',
                                                  symmetrical=False)
    product_prerequisites = models.ManyToManyField('ProductPrerequisite', related_name='blueprint_requirements',
                                                   symmetrical=False)
    thumbnail_image = models.ForeignKey(URL, on_delete=models.PROTECT, related_name='blueprint_thumbnail', null=True)
    illustration_images = models.ManyToManyField(OffsetImageURL, related_name='blueprint_illustration',
                                                 symmetrical=False)
    description_images = models.ManyToManyField(URL, related_name='blueprint_description_image', symmetrical=False)
    retail_price = models.FloatField(verbose_name='Retail Price', default=0, null=False)
    retail_price_per_unit = models.FloatField(verbose_name='Retail Price per unit', default=0, null=False)
    retail_unit_measurement = models.CharField(max_length=255, null=True, blank=True)
    internal_cost = models.FloatField(default=0, null=False)

    component_factor = models.FloatField(default=None, null=True)
    build_time = models.PositiveIntegerField(default=0, null=False)


    def isEmpty(self):
        if len(self.atomic_prerequisites.all()) == 0 and len(self.product_prerequisites.all()) == 0:
            return True
        else:
            return False

    def getComponentFactor(self):
        if self.component_factor is None:
            # Do CF calculation
            total = 0
            for a_preq in self.atomic_prerequisites:
                total += a_preq.atomic_component.getComponentFactor()
            for p_preq in self.product_prerequisites:
                total += p_preq.product.blueprint.getComponentFactor()
            return total
        else:
            return self.component_factor


class BlueprintAttribute(TimestampedModel):

    blueprint = models.ForeignKey(Blueprint, on_delete=models.PROTECT, related_name="blueprint_attribute", null=False)
    key = models.CharField(max_length=255, blank=False, null=False)
    value = models.CharField(max_length=255, blank=False, null=False)


class ProductPrerequisite(Prerequisite):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='requires',
                                null=True)
    product_group = models.ForeignKey('ProductGroup', on_delete=models.PROTECT, related_name='allowed_group', null=True)

    def save(self, *args, **kwargs):
        if self.product is None and self.product_group is None:
            raise ValidationError(
                _('ProductPrerequisite has no assigned product or product-group'),
                code='invalid',
            )
        super(ProductPrerequisite, self).save(*args, **kwargs)


class ProductSpecification(Specification):
    selected_component = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='using',
                                           null=True)
    prerequisite = models.ForeignKey(ProductPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                     null=True)


class Product(TimestampedModel):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=3)
    availability = models.IntegerField(null=False, default=0)
    blueprint = models.ForeignKey(Blueprint, on_delete=models.PROTECT, related_name='based_on', null=False)
    atomic_specifications = models.ManyToManyField(AtomicSpecification, related_name='atomic_specification',
                                                   symmetrical=False)
    product_specifications = models.ManyToManyField(ProductSpecification, related_name='product_specification',
                                                    symmetrical=False)
    attribute = models.ManyToManyField(Attribute, related_name='product_attr')
    thumbnail_image = models.ForeignKey(URL, on_delete=models.PROTECT, related_name='thumbnail_image', null=True)
    illustration_images = models.ManyToManyField(OffsetImageURL, related_name='illustration_image',
                                                 symmetrical=False)
    description_images = models.ManyToManyField(URL, related_name='description_image', symmetrical=False)
    retail_price = models.FloatField(verbose_name='Retail Price', default=0, null=False)
    retail_price_per_unit = models.FloatField(verbose_name='Retail Price per unit', default=0, null=False)
    retail_unit_measurement = models.CharField(max_length=255, null=True, blank=True)
    internal_cost = models.FloatField(default=0, null=False)

    component_factor = models.FloatField(default=None, null=True)

    def getComponentFactor(self):
        if self.component_factor is not None:
            return self.component_factor
        else:
            # sum all CF from all prerequisites
            total = 0
            for spec in self.atomic_specifications.all():
                total = total + spec.selected_component.getComponentFactor()
            for spec in self.product_specifications.all():
                total = total + spec.selected_component.getComponentFactor()

            return total


    def validate(self):
        """
        Valiate quantity following prerequisite constraint
        :return: Bool
        """
        # Atomic
        prerequisite_list = [p for p in self.blueprint.atomic_prerequisites.all()]
        specification_list = [s for s in self.atomic_specifications.all()]
        for prerequisite in prerequisite_list:
            # Keep track of all quantity specified for prerequisite
            specified_quantity = 0
            for specification in specification_list:
                if specification.prerequisite == prerequisite:  # Matching specification
                    # Check if specification's target atomic component is within
                    # prerequisites bound
                    if specification.selected_component != prerequisite.atomic_component:
                        if prerequisite.atomic_group is None:
                            # specification not pointed directly, and no group
                            raise ValidationError(
                                _('Invalid component: %(component)s'),
                                code='invalid',
                                params={'component': specification.selected_component.stock_code},
                            )
                        elif specification.selected_component not in prerequisite.atomic_group:
                            # specification not pointed directly, not in assigned group
                            raise ValidationError(
                                _('Invalid component: %(component)s'),
                                code='invalid',
                                params={'component': specification.selected_component.stock_code},
                            )
                    else:
                        specified_quantity += specification.quantity

            # If specifications not met the minimum quantity
            if specified_quantity < prerequisite.min_quantity:
                raise ValidationError(
                    _('Insufficient specification: %(component)s requires minimum of %(min)s, given %(num)s'),
                    code='invalid',
                    params={
                        'component': prerequisite.atomic_component.stock_code,
                        'min': prerequisite.min_quantity,
                        'num': specified_quantity,
                    }
                )

            # If specifications not met the minimum quantity
            if specified_quantity > prerequisite.max_quantity:
                raise ValidationError(
                    _('Specifications exceeded maximum limit: %(component)s has a maximum of %(max)s, given %(num)s'),
                    code='invalid',
                    params={
                        'component': prerequisite.atomic_component.stock_code,
                        'max': prerequisite.max_quantity,
                        'num': specified_quantity,
                    }
                )

        # Product
        prerequisite_list = [p for p in self.blueprint.product_prerequisites.all()]
        specification_list = [s for s in self.product_specifications.all()]
        for prerequisite in prerequisite_list:
            # Keep track of all quantity specified for prerequisite
            specified_quantity = 0
            for specification in specification_list:
                if specification.prerequisite == prerequisite:  # Matching specification
                    # Check if specification's target atomic component is within
                    # prerequisites bound
                    if specification.selected_component != prerequisite.product:
                        if prerequisite.product_group is None:
                            # specification not pointed directly, and no group
                            raise ValidationError(
                                _('Invalid component: %(component)s'),
                                code='invalid',
                                params={'component': specification.selected_component.name},
                            )
                        elif specification.selected_component not in prerequisite.product_group:
                            # specification not pointed directly, not in assigned group
                            raise ValidationError(
                                _('Invalid component: %(component)s'),
                                code='invalid',
                                params={'component': specification.selected_component.name},
                            )
                    else:
                        specified_quantity += specification.quantity

            # If specifications not met the minimum quantity
            if specified_quantity < prerequisite.min_quantity:
                raise ValidationError(
                    _('Insufficient specification: Prerequisite %(id)s requires minimum of %(min)s, given %(num)s'),
                    code='invalid',
                    params={
                        'id': prerequisite.id,
                        'min': prerequisite.min_quantity,
                        'num': specified_quantity,
                    }
                )

            # If specifications not met the minimum quantity
            if specified_quantity > prerequisite.max_quantity:
                raise ValidationError(
                    _(
                        'Specifications exceeded maximum limit: Prerequisite %(id)s has a maximum of %(max)s, given %(num)s'),
                    code='invalid',
                    params={
                        'id': prerequisite.id,
                        'max': prerequisite.max_quantity,
                        'num': specified_quantity,
                    }
                )


class BlueprintGroup(Group):
    members = models.ManyToManyField(Blueprint, related_name='members')


class ProductGroup(Group):
    members = models.ManyToManyField(Product, related_name='members')

