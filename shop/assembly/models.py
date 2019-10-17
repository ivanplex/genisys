from django.db import models
from shop.models import TimestampedModel
from shop.relations.models import Prerequisite, Specification
from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification
from shop.attribute.models import KeyValueAttribute
from shop.group.models import Group


class BlueprintAttribute(KeyValueAttribute):
    blueprint = models.ForeignKey('Blueprint', on_delete=models.CASCADE,
                                  related_name='blueprint_attribute', null=False)


class Blueprint(TimestampedModel):
    name = models.CharField(max_length=250)
    atomic_prerequisites = models.ManyToManyField(AtomicPrerequisite, related_name='atomic_requirements', symmetrical=False)
    product_prerequisites = models.ManyToManyField('ProductPrerequisite', related_name='blueprint_requirements',
                                                   symmetrical=False)

    def attribute(self):
        attr = BlueprintAttribute.objects.filter(blueprint=self)
        return attr

    def isEmpty(self):
        if len(self.atomic_prerequisites.all()) == 0 and len(self.product_prerequisites.all()) == 0:
            return True
        else:
            return False

    def getLocalAtomicPrerequisites(self):
        """
        Return local AtomicPrerequisite only
        :return: list[AtomicRequirement]
        """
        l = []
        for prereq in self.atomic_prerequisites.all():
            l.append(prereq)
        return l

    def allAtomicPrerequisites(self):
        """
        Return all atomic prerequisites recursively
        return list instead of queryset

        :return: list[AtomicRequirement]
        """
        if len(self.product_prerequisites.all()) == 0:
            # If no further blueprint dependencies
            return self.getLocalAtomicPrerequisites()
        else:
            atomic_prereq = self.getLocalAtomicPrerequisites()
            for prereq in self.product_prerequisites.all():
                atomic_prereq.extend(prereq.product.blueprint.allAtomicPrerequisites())
            return atomic_prereq

    def getLocalBuildPrerequisites(self):
        """
        Return local BuildPrerequisite only
        :return: list[AtomicRequirement]
        """
        l = []
        for prereq in self.product_prerequisites.all():
            l.append(prereq)
        return l

    def allBuildPrerequisites(self):
        """
        Return all product prerequisites recursively
        return list instead of queryset

        :return: list[AtomicRequirement]
        """
        if len(self.product_prerequisites.all()) == 0:
            # If no further blueprint dependencies
            return []
        else:
            productPrereq = self.getLocalBuildPrerequisites()
            for prereq in self.product_prerequisites.all():
                productPrereq.extend(prereq.product.blueprint.getLocalBuildPrerequisites())
            return productPrereq

    def map_prerequisites(self):
        struct = {}
        struct['name'] = self.name
        struct['atomic_prereq'] = self.getLocalAtomicPrerequisites()
        struct['product_prereq'] = []

        for prereq in self.product_prerequisites.all():
            struct['product_prereq'].append(prereq.product.blueprint.map_prerequisites())
        return struct


class ProductPrerequisite(Prerequisite):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='requires',
                                null=False)


class ProductSpecification(Specification):
    product_prereq = models.ForeignKey(ProductPrerequisite, on_delete=models.PROTECT, related_name='build_with',
                                       null=False)

    def validate(self):
        """
        Valiate quantity following prerequisite constraint
        :return: Bool
        """
        return True if self.product_prereq.min_quantity <= self.quantity <= self.product_prereq.max_quantity else False


class ProductAttribute(KeyValueAttribute):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                  related_name='product_attribute', null=False)


class Product(TimestampedModel):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=3)
    availability = models.IntegerField(null=False, default=0)

    blueprint = models.ForeignKey(Blueprint, on_delete=models.PROTECT, related_name='based_on', null=False)

    atomic_specifications = models.ManyToManyField(AtomicSpecification, related_name='atomic_specification', symmetrical=False)
    product_specifications = models.ManyToManyField(ProductSpecification, related_name='product_specification', symmetrical=False)

    def hasProductPrerequisite(self):
        return False if not self.blueprint.product_prerequisites.all() else True


    def validate(self):
        """
        Validate the following
        - Prerequisite compliance
        - Prerequisite quantity constraints
        :return:
        """
        return True if self.validate_spec() and self.prerequisiteAudit().fulfilled() else False

    def validate_spec(self):
        """
        Valiate quantity following prerequisite constraint
        :return: Bool
        """
        # TODO: Make this recursive
        for spec in self.atomic_specifications.all():
            if spec.validate():
                continue
            else:
                return False
        return True

    def prerequisiteAudit(self):

        deficit = PrerequisiteAudit()

        deficit.deficit = [x for x in self.blueprint.getLocalAtomicPrerequisites()
                     if x not in self.getLocalAtomicPrerequisites()]
        deficit.surplus = [x for x in self.getLocalAtomicPrerequisites()
                     if x not in self.blueprint.getLocalAtomicPrerequisites()]

        # Add blueprint deficit
        blueprint_spec_prereq = [x.product_prereq for x in self.getLocalBuildSpecifications()]
        blueprint_deficit = [x for x in self.blueprint.getLocalBuildPrerequisites()
                     if x not in blueprint_spec_prereq]

        blueprint_surplus = [x for x in blueprint_spec_prereq
                     if x not in self.blueprint.getLocalBuildPrerequisites()]
        deficit.deficit.extend(blueprint_deficit)
        deficit.deficit.extend(blueprint_surplus)

        return deficit

    def getLocalAtomicSpecifications(self):
        """
        Return local AtomicSpecification only
        :return: list[AtomicSpecification]
        """
        l = []
        for spec in self.atomic_specifications.all():
            l.append(spec)
        return l

    def getLocalAtomicPrerequisites(self):
        """
        Return a list of AtomicPrerequsites
        specified by all atomicSpecifications
        in the blueprint

        :return: list[AtomicPrerequsites]
        """
        l = []
        for spec in self.atomic_specifications.all():
            l.append(spec.atomic_prereq)
        return l

    def getLocalBuildSpecifications(self):
        """
        Return local BuildSpecification only
        :return: list[AtomicSpecification]
        """
        l = []
        for spec in self.product_specifications.all():
            l.append(spec)
        return l

    def map_spec(self):
        struct = {}
        struct['name'] = self.name
        struct['atomic_spec'] = self.getLocalAtomicSpecifications()
        struct['product_spec'] = []
        struct['audit'] = self.prerequisiteAudit().__str__()

        for spec in self.product_specifications.all():
            struct['product_spec'].append(spec.product_prereq.product.map_spec())
        return struct


class BlueprintGroup(Group):
    members = models.ManyToManyField(Blueprint, related_name='members')


class ProductGroup(Group):
    members = models.ManyToManyField(Product, related_name='members')


#TODO: Redefine how to handle Audits
class PrerequisiteAudit:
    """
    Prerequisite auditing for products
    """
    def __init__(self):
        self.deficit = []
        self.surplus = []

    def fulfilled(self):
        if not self.deficit and not self.surplus:
            return True
        else:
            return False

    def __str__(self):
        return "Audit: Deficit-{}: Surplus-{}".format(len(self.deficit), len(self.surplus))

