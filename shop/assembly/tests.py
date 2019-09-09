from django.test import TestCase
from shop.models import AtomicComponent
from shop.concept.models import Blueprint, AtomicPrerequisite, BlueprintPrerequisite
from .models import AtomicSpecification, Build, BlueprintSpecification


class Build_validate_legal_atomic_spec(TestCase):

    def setUp(self):
        min = 4
        max = 8
        spec_quantity = 6

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereq = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=min, max_quantity=max)
        self.blueprint.atomic_prerequisites.add(self.atomic_prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)
        self.spec = AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereq, quantity=spec_quantity)
        self.build.atomic_specifications.add(self.spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.validate(), True)

class Build_validate_illegal_atomic_spec(TestCase):

    def setUp(self):
        min = 4
        max = 8
        spec_quantity = 20

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereq = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=min, max_quantity=max)
        self.blueprint.atomic_prerequisites.add(self.atomic_prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)
        self.spec = AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereq, quantity=spec_quantity)
        self.build.atomic_specifications.add(self.spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.validate(), False)

class Build_validate_legal_multiple_atomic_spec(TestCase):

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
            min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=6)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.validate(), True)

class Build_validate_illegal_multiple_atomic_spec(TestCase):

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
            min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=20)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.validate(), False)

class Build_Audit_prerequisite(TestCase):

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
            min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=20)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.prerequisiteAudit().fulfilled(), True)

class Build_Audit_prerequisite_deficit(TestCase):
    """
    Prerequisite Audit with a deficit
    """

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
            min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.prerequisiteAudit().fulfilled(), False)
        self.assertEqual(self.build.prerequisiteAudit().deficit, [self.atomic_prereqs[1]])
        self.assertEqual(self.build.prerequisiteAudit().surplus, [])

class Build_Audit_prerequisite_surplus(TestCase):
    """
    Prerequisite Audit with a surplus
    """

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
            min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)

        self.additional_pre = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='C-Bolt', availability=300),
            min_quantity=4, max_quantity=8)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.additional_pre, quantity=6)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.prerequisiteAudit().fulfilled(), False)
        self.assertEqual(self.build.prerequisiteAudit().deficit, [])
        self.assertEqual(self.build.prerequisiteAudit().surplus, [self.additional_pre])

class Build_Audit_prerequisite_surplus(TestCase):
    """
    Prerequisite Audit with both deficit and surplus
    """

    def setUp(self):

        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereqs = [
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
            min_quantity=4, max_quantity=8)
        ]

        for prereq in self.atomic_prereqs:
            self.blueprint.atomic_prerequisites.add(prereq)
        self.blueprint.save()

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)

        self.additional_pre = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='C-Bolt', availability=300),
            min_quantity=4, max_quantity=8)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.additional_pre, quantity=6)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()

    def test(self):
        self.assertEqual(self.build.prerequisiteAudit().fulfilled(), False)
        self.assertEqual(self.build.prerequisiteAudit().deficit, [self.atomic_prereqs[1]])
        self.assertEqual(self.build.prerequisiteAudit().surplus, [self.additional_pre])


# class Build_fulfilment_additional_spec_prerequisite(TestCase):
#     """
#     When a build has extra specification
#     """
#
#     def setUp(self):
#
#         self.blueprint = Blueprint.objects.create(name="Table")
#         self.atomic_prereqs = [
#             AtomicPrerequisite.objects.create(
#             atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
#             min_quantity=4, max_quantity=8),
#             AtomicPrerequisite.objects.create(
#             atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
#             min_quantity=4, max_quantity=8)
#         ]
#
#         for prereq in self.atomic_prereqs:
#             self.blueprint.atomic_prerequisites.add(prereq)
#         self.blueprint.save()
#
#         self.build = Build.objects.create(name='Table', blueprint=self.blueprint)
#
#         self.atomic_specs = [
#             AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
#             AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=20),
#             AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=7)
#         ]
#         for spec in self.atomic_specs:
#             self.build.atomic_specifications.add(spec)
#         self.build.save()
#
#     def test(self):
#         self.assertEqual(self.build.ifFulfilPrerequisite(), False)

#TODO: Check if specifications comply with every prerequisite


# class Build_PositiveAvailability_SingleLayer_TestCase(TestCase):
#
#     def setUp(self):
#         supply = 300
#         demand = 4
#
#         self.blueprint = Blueprint.objects.create(name="Table")
#         self.atomic_prereq = AtomicPrerequisite.objects.create(
#             atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply),
#             quantity=demand)
#         self.blueprint.atomic_requirements.add(self.atomic_prereq)
#
#         self.b = Build.objects.create(name='Table')
#
#         self.b.atomic_requirements.add(r)
#         self.b.save()
#
#     def test(self):
#         self.assertEqual(self.b.available(), True)

#
# class Blueprint_NegativeAvailability_SingleLayer_TestCase(TestCase):
#
#     def setUp(self):
#         supply = 3
#         demand = 4
#
#         self.b = Build.objects.create(name='Table')
#         r = AtomicSpecification.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
#         self.b.atomic_requirements.add(r)
#         self.b.save()
#
#     def test(self):
#         self.assertEqual(self.b.available(), False)
#
#
# class Blueprint_PositiveAvailability_MultiLayer_TestCase(TestCase):
#
#     def setUp(self):
#         supply = 300
#         demand = 4
#
#         self.table = Build.objects.create(name='table')
#         r = AtomicSpecification.objects.create(
#             atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
#         self.table.atomic_requirements.add(r)
#         self.table.save()
#         br = BlueprintSpecification.objects.create(blueprint_component=self.table, quantity=1)
#
#         self.tableset = Build.objects.create(name='tableset')
#         self.tableset.blueprint_requirements.add(br)
#         self.tableset.save()
#
#     def test(self):
#         """
#         Test multilayer availability
#         :return:
#         """
#         self.assertEqual(self.tableset.available(), True)
#
# class Blueprint_NegativeAvailability_MultiLayer_TestCase(TestCase):
#
#     def setUp(self):
#         supply = 3
#         demand = 4
#
#         self.table = Build.objects.create(name='table')
#         r = AtomicSpecification.objects.create(
#             atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=supply), quantity=demand)
#         self.table.atomic_requirements.add(r)
#         self.table.save()
#         br = BlueprintSpecification.objects.create(blueprint_component=self.table, quantity=1)
#
#
#         self.tableset = Build.objects.create(name='tableset')
#         self.tableset.blueprint_requirements.add(br)
#         self.tableset.save()
#
#     def test(self):
#         """
#         Test multilayer availability
#         :return:
#         """
#         self.assertEqual(self.tableset.available(), False)