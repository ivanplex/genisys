from django.test import TestCase
from .models import Blueprint, Build, BuildSpecification, BuildPrerequisite, PrerequisiteAudit
from shop.atomic.models import AtomicComponent, AtomicSpecification, AtomicPrerequisite

class Build_Validate_Atomic_Spec(TestCase):

    def setUp(self):
        min = 4
        max = 8


        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prereq = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
            min_quantity=min, max_quantity=max)
        self.blueprint.atomic_prerequisites.add(self.atomic_prereq)
        self.blueprint.save()

    def test_winthin_bound(self):
        """
        BuildSpecification following buildPrerequisite
        """
        spec_quantity = 6

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)
        self.spec = AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereq, quantity=spec_quantity)
        self.build.atomic_specifications.add(self.spec)
        self.build.save()

        self.assertEqual(self.build.validate_spec(), True)

    def test_out_of_bound(self):
        """
        BuildSpecification NOT following buildPrerequisite
        """
        spec_quantity = 20

        self.build = Build.objects.create(name='Table', blueprint=self.blueprint)
        self.spec = AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereq, quantity=spec_quantity)
        self.build.atomic_specifications.add(self.spec)
        self.build.save()

        self.assertEqual(self.build.validate_spec(), True)

class Build_Validate_Multiple_Atomic_Spec(TestCase):

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



    def test_within_bound(self):
        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=6)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()
        self.assertEqual(self.build.validate_spec(), True)

    def test_out_of_bound(self):
        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prereqs[1], quantity=20)
        ]
        for spec in self.atomic_specs:
            self.build.atomic_specifications.add(spec)
        self.build.save()
        self.assertEqual(self.build.validate_spec(), True)

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

class Build_Audit_prerequisite_deficitANDsurplus(TestCase):
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

class Build_Audit_fulfillment(TestCase):

    def setUp(self):

        self.audit = PrerequisiteAudit()

    def test(self):
        self.assertEqual(self.audit.fulfilled(), True)

class Build_Audit_fulfillment_both(TestCase):

    def setUp(self):

        self.audit = PrerequisiteAudit()
        self.audit.deficit.append(1)
        self.audit.surplus.append(1)

    def test(self):
        self.assertEqual(self.audit.fulfilled(), False)

class Build_Audit_fulfillment_deficit(TestCase):

    def setUp(self):

        self.audit = PrerequisiteAudit()
        self.audit.deficit.append(1)

    def test(self):
        self.assertEqual(self.audit.fulfilled(), False)
#
class Build_Audit_fulfillment_surplus(TestCase):

    def setUp(self):

        self.audit = PrerequisiteAudit()
        self.audit.surplus.append(1)

    def test(self):
        self.assertEqual(self.audit.fulfilled(), False)

class Build_Audit_prerequisite_recursive(TestCase):
    def setUp(self):

        # Define atomic variables
        a_table_top = AtomicComponent.objects.create(stock_code='Table-Top', availability=50)
        a_table_leg = AtomicComponent.objects.create(stock_code='Table-leg', availability=700)
        a_chair = AtomicComponent.objects.create(stock_code='chair', availability=300)

        # define table
        tableBlueprint = Blueprint.objects.create(name="Table")

        AP_table_top = AtomicPrerequisite.objects.create(atomic_component=a_table_top, min_quantity=1, max_quantity=1)
        AP_table_leg = AtomicPrerequisite.objects.create(atomic_component=a_table_leg, min_quantity=4, max_quantity=8)
        table_atomic_prereqs = [AP_table_top, AP_table_leg]

        for prereq in table_atomic_prereqs:
            tableBlueprint.atomic_prerequisites.add(prereq)
        tableBlueprint.save()

        # Build table
        tableBuild = Build.objects.create(name='Table', blueprint=tableBlueprint)
        AS_table_top = AtomicSpecification.objects.create(atomic_prereq=AP_table_top, quantity=1)
        AS_table_leg = AtomicSpecification.objects.create(atomic_prereq=AP_table_leg, quantity=4)
        tableBuild_atomic_spec = [AS_table_top, AS_table_leg]
        for spec in tableBuild_atomic_spec:
            tableBuild.atomic_specifications.add(spec)
        tableBuild.save()

        # define table-set
        tableSetBlueprint = Blueprint.objects.create(name="tableSet")
        tableSetBuildPrereq = BuildPrerequisite.objects.create(
            build=tableBuild, min_quantity=1, max_quantity=1)
        tableSetAtomicPrereq = AtomicPrerequisite.objects.create(
            atomic_component=a_chair, min_quantity=2, max_quantity=4)
        tableSetBlueprint.build_prerequisites.add(tableSetBuildPrereq)
        tableSetBlueprint.atomic_prerequisites.add(tableSetAtomicPrereq)
        tableSetBlueprint.save()

        # build table-set
        self.tableSetBuild = Build.objects.create(name='TableSet', blueprint=tableSetBlueprint)
        AS_tableset_chairs = AtomicSpecification.objects.create(atomic_prereq=tableSetAtomicPrereq, quantity=4)
        self.tableSetBuild.atomic_specifications.add(AS_tableset_chairs)

        self.tableSetBuild.build_specifications.add(
            BuildSpecification.objects.create(build_prereq=tableSetBuildPrereq, quantity=1)
        )
        self.tableSetBuild.save()

    def test(self):
        self.assertEqual(self.tableSetBuild.prerequisiteAudit().fulfilled(), True)

class Build_has_prerequsite(TestCase):
    def setUp(self):
        b2_Blueprint = Blueprint.objects.create(name="LowerBlueprint")
        b2 = Build.objects.create(name="LowerBuild", blueprint=b2_Blueprint)

        b1_Blueprint = Blueprint.objects.create(name="UpperBlueprint")
        b1_build_prereq = BuildPrerequisite.objects.create(build=b2, min_quantity=1, max_quantity=1)
        b1_Blueprint.build_prerequisites.add(b1_build_prereq)

        self.b1 = Build.objects.create(name="UpperBuild", blueprint=b1_Blueprint)

    def test(self):
        self.assertEqual(self.b1.hasBuildPrerequisite(), True)

class Build_has_no_prerequsite(TestCase):
    def setUp(self):
        b2_Blueprint = Blueprint.objects.create(name="LowerBlueprint")
        self.b2 = Build.objects.create(name="LowerBuild", blueprint=b2_Blueprint)

    def test(self):
        self.assertEqual(self.b2.hasBuildPrerequisite(), False)

#TODO: Check if atomic variables are available