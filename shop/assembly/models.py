from django.db import models
from shop.models import TimestampedModel
from shop.relations.models import Prerequisite, Specification
from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification
from shop.attribute.models import KeyValueAttribute
from shop.group.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BlueprintAttribute(KeyValueAttribute):
    blueprint = models.ForeignKey('Blueprint', on_delete=models.CASCADE,
                                  related_name='blueprint_attribute', null=False)


class Blueprint(TimestampedModel):
    name = models.CharField(max_length=250)
    atomic_prerequisites = models.ManyToManyField(AtomicPrerequisite, related_name='atomic_requirements',
                                                  symmetrical=False)
    product_prerequisites = models.ManyToManyField('ProductPrerequisite', related_name='blueprint_requirements',
                                                   symmetrical=False)

    def attribute(self):
        attr = BlueprintAttribute.objects.filter(blueprint=self)
        return attr


class ProductPrerequisite(Prerequisite):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='requires',
                                null=False)


class ProductSpecification(Specification):
    selected_component = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='using',
                                           null=True)
    prerequisite = models.ForeignKey(ProductPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                     null=True)


class ProductAttribute(KeyValueAttribute):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='product_attribute', null=False)


class Product(TimestampedModel):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=3)
    availability = models.IntegerField(null=False, default=0)

    blueprint = models.ForeignKey(Blueprint, on_delete=models.PROTECT, related_name='based_on', null=False)

    atomic_specifications = models.ManyToManyField(AtomicSpecification, related_name='atomic_specification',
                                                   symmetrical=False)
    product_specifications = models.ManyToManyField(ProductSpecification, related_name='product_specification',
                                                    symmetrical=False)

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

        # TODO: VALIDATE PRODUCT


class BlueprintGroup(Group):
    members = models.ManyToManyField(Blueprint, related_name='members')


class ProductGroup(Group):
    members = models.ManyToManyField(Product, related_name='members')

