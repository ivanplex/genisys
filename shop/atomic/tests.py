from django.test import TestCase
from .models import AtomicComponent
from django.core.exceptions import ValidationError
from shop.assembly.models import Blueprint, BuildPrerequisite, Build, BuildSpecification
from shop.atomic.models import AtomicPrerequisite, AtomicSpecification, AtomicComponent


class AtomicComponent_create_TestCase(TestCase):
    def test(self):
        """
        Test AtomicComponent creation
        """
        try:
            a = AtomicComponent()
            a.save()
            self.fail("Violation integrity")
        except ValidationError:
            pass

class Blueprint_empty_valid_TestCase(TestCase):

    def setUp(self):
        self.b = Blueprint.objects.create(name="Table")
    def test(self):
        """
        Test empty Blueprint
        """
        self.assertEqual(self.b.isEmpty(), True)

class Blueprint_assign_atomic_only_TestCase(TestCase):
    def test(self):
        """
        Test assigning 1 atomic component
        """
        a = AtomicComponent.objects.create(stock_code="TEST", part_code="Test", availability=700)
        ar = AtomicPrerequisite.objects.create(atomic_component=a, min_quantity=4, max_quantity=4)

        try:
            b = Blueprint.objects.create(name="Table")
            b.atomic_prerequisites.add(ar)
            b.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_assign_multiple_atomic_TestCase(TestCase):
    def test(self):
        """
        Test assign multiple atomicComponent
        """

        component = [
            AtomicComponent.objects.create(stock_code="Apple", part_code="Apple", availability=700),
            AtomicComponent.objects.create(stock_code="Orange", part_code="Orange", availability=400),
            AtomicComponent.objects.create(stock_code="Banana", part_code="Banana", availability=200)
        ]

        c_req = []
        for c in component:
            c_req.append(AtomicPrerequisite.objects.create(atomic_component=c, min_quantity=2, max_quantity=2))

        try:
            b = Blueprint.objects.create(name="Table")

            # Add all AtomicComponent requirements to Blueprint
            for req in c_req:
                b.atomic_prerequisites.add(req)

            b.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_assign_blueprint_TestCase(TestCase):
    def test(self):
        """
        Test assigning blueprint requirement on blueprint
        """
        try:
            # define
            a = AtomicComponent.objects.create(stock_code="TEST", part_code="Test", availability=700)
            ar = AtomicPrerequisite.objects.create(atomic_component=a, min_quantity=4, max_quantity=4)
            b = Blueprint.objects.create(name="Table")
            b.atomic_prerequisites.add(ar)
            b.save()

            # build
            tableBuild = Build.objects.create(name="table", blueprint=b)
            tableBuildAtomicSpec = AtomicSpecification.objects.create(atomic_prereq=ar, quantity=4)
            tableBuild.atomic_specifications.add(tableBuildAtomicSpec)

            b_set = Blueprint.objects.create(name="Table_set")
            b_set_req = BuildPrerequisite.objects.create(build=tableBuild, min_quantity=2, max_quantity=2)
            b_set.build_prerequisites.add(b_set_req)
            b_set.save()
        except:
            self.fail('Creation of Blueprint object failed.')

class Blueprint_TrueEmpty_TestCase(TestCase):

    def setUp(self):
        self.table = Blueprint.objects.create(name='table')

    def test(self):
        """
        True empty of a Blueprint
        """
        self.assertEqual(self.table.isEmpty(), True)

class Blueprint_FalseEmpty_1_TestCase(TestCase):

    def setUp(self):
        self.table = Blueprint.objects.create(name='table')
        r = AtomicPrerequisite.objects.create(atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300), min_quantity=2, max_quantity=2)
        self.table.atomic_prerequisites.add(r)
        self.table.save()

    def test(self):
        """
        False empty when blueprint contains atomicComponent
        """
        self.assertEqual(self.table.isEmpty(), False)

class Blueprint_FalseEmpty_2_TestCase(TestCase):

    def setUp(self):

        # atomic
        atom = AtomicComponent.objects.create(stock_code='U-Bolt', availability=300)

        # define table
        table = Blueprint.objects.create(name='table')
        r = AtomicPrerequisite.objects.create(atomic_component=atom, min_quantity=2, max_quantity=2)
        table.atomic_prerequisites.add(r)
        table.save()

        # build table
        tableBuild = Build.objects.create(name="table", blueprint=table)
        tableAtomicSpec = AtomicSpecification.objects.create(atomic_prereq=r, quantity=2)
        tableBuild.atomic_specifications.add(tableAtomicSpec)
        tableBuild.save()

        br = BuildPrerequisite.objects.create(build=tableBuild, min_quantity=1, max_quantity=1)

        # define table-set
        self.tableset = Blueprint.objects.create(name='tableSet')
        tablesetBuildPrereq = BuildPrerequisite.objects.create(build=tableBuild, min_quantity=1, max_quantity=1)
        self.tableset.build_prerequisites.add(tablesetBuildPrereq)
        self.tableset.save()

    def test(self):
        """
        False empty when child of a blueprint contains atomicPrereq
        """
        self.assertEqual(self.tableset.isEmpty(), False)

class Blueprint_RecursiveAtomicPrereq_TestCase(TestCase):
    """
    Test aggregation of all atomic dependency recursively under blueprint

    Scenario: Ikea table set

    Table-set contains 1 table (blueprint) and 4 chairs (blueprint)
    and a instruction manual (atomic)

    A table contains 1 table-top, 4 legs, 4 screws
    A chair contains a backplate and 4 legs, 4 screws

    Validate list
    """

    def setUp(self):

        # Atomic
        self.manual = AtomicComponent.objects.create(stock_code="man", availability=5)
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)
        self.backplate = AtomicComponent.objects.create(stock_code="backplate", availability=15)

        # Define table
        tableBlueprint = Blueprint.objects.create(name="table")
        table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
        table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        tableAtomicPrereq = [table_AP_1, table_AP_2, table_AP_3]
        for req in tableAtomicPrereq:
            tableBlueprint.atomic_prerequisites.add(req)
        tableBlueprint.save()

        # Build table
        tableBuild = Build.objects.create(name='table', blueprint=tableBlueprint)
        table_AS_1 = AtomicSpecification.objects.create(atomic_prereq=table_AP_1, quantity=1)
        table_AS_2 = AtomicSpecification.objects.create(atomic_prereq=table_AP_2, quantity=4)
        table_AS_3 = AtomicSpecification.objects.create(atomic_prereq=table_AP_3, quantity=4)
        tableBuildSpec = [table_AS_1, table_AS_2, table_AS_3]
        for spec in tableBuildSpec:
            tableBuild.atomic_specifications.add(spec)
        tableBuild.save()

        # Define chair
        chairBlueprint = Blueprint.objects.create(name="chair")
        chair_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.backplate, min_quantity=1, max_quantity=1)
        chair_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        chair_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        chairAtomicPrereq = [chair_AP_1, chair_AP_2, chair_AP_3]
        for prereq in chairAtomicPrereq:
            chairBlueprint.atomic_prerequisites.add(prereq)
        chairBlueprint.save()

        # Build chair
        chairBuild = Build.objects.create(name="chair", blueprint=chairBlueprint)
        chair_AS_1 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_1, quantity=1)
        chair_AS_2 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_2, quantity=4)
        chair_AS_3 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_3, quantity=4)
        chairAtomicSpec = [chair_AS_1, chair_AS_2, chair_AS_3]
        for spec in chairAtomicSpec:
            chairBuild.atomic_specifications.add(spec)
        chairBuild.save()

        # define table-set
        self.tablesetBuildprint = Blueprint.objects.create(name="tableset")
        tablesetAtomicPrereq = AtomicPrerequisite.objects.create(atomic_component=self.manual, min_quantity=1, max_quantity=1)
        tablesetBuildPrereq = [
            BuildPrerequisite.objects.create(build=tableBuild, min_quantity=1, max_quantity=1),
            BuildPrerequisite.objects.create(build=chairBuild, min_quantity=1, max_quantity=4)
        ]
        self.tablesetBuildprint.atomic_prerequisites.add(tablesetAtomicPrereq)
        for bpReq in tablesetBuildPrereq:
            self.tablesetBuildprint.build_prerequisites.add(bpReq)
        self.tablesetBuildprint.save()

        # create a list of all requirements
        self.allAtomicRequirements = tableAtomicPrereq + chairAtomicPrereq + [tablesetAtomicPrereq]

    def test(self):
        """
        Test recursive collection of all AtomicRequirements of a Blueprint
        :return:
        """
        self.assertEqual(set(self.tablesetBuildprint.allAtomicPrerequisites()), set(self.allAtomicRequirements))

class Blueprint_RecursiveBuildPrereq_TestCase(TestCase):
    """
    Test aggregation of all atomic specification recursively under build

    Scenario: Ikea table set

    Table-set contains 1 table (blueprint) and 4 chairs (blueprint)
    and a instruction manual (atomic)

    A table contains 1 table-top, 4 legs, 4 screws
    A chair contains a backplate and 4 legs, 4 screws

    Validate
    """

    def setUp(self):

        # Atomic
        self.manual = AtomicComponent.objects.create(stock_code="man", availability=5)
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)
        self.backplate = AtomicComponent.objects.create(stock_code="backplate", availability=15)

        # Define table
        tableBlueprint = Blueprint.objects.create(name="table")
        table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
        table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        tableAtomicPrereq = [table_AP_1, table_AP_2, table_AP_3]
        for req in tableAtomicPrereq:
            tableBlueprint.atomic_prerequisites.add(req)
        tableBlueprint.save()

        # Build table
        tableBuild = Build.objects.create(name='table', blueprint=tableBlueprint)
        table_AS_1 = AtomicSpecification.objects.create(atomic_prereq=table_AP_1, quantity=1)
        table_AS_2 = AtomicSpecification.objects.create(atomic_prereq=table_AP_2, quantity=4)
        table_AS_3 = AtomicSpecification.objects.create(atomic_prereq=table_AP_3, quantity=4)
        tableBuildSpec = [table_AS_1, table_AS_2, table_AS_3]
        for spec in tableBuildSpec:
            tableBuild.atomic_specifications.add(spec)
        tableBuild.save()

        # Define chair
        chairBlueprint = Blueprint.objects.create(name="chair")
        chair_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.backplate, min_quantity=1, max_quantity=1)
        chair_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        chair_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        chairAtomicPrereq = [chair_AP_1, chair_AP_2, chair_AP_3]
        for prereq in chairAtomicPrereq:
            chairBlueprint.atomic_prerequisites.add(prereq)
        chairBlueprint.save()

        # Build chair
        chairBuild = Build.objects.create(name="chair", blueprint=chairBlueprint)
        chair_AS_1 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_1, quantity=1)
        chair_AS_2 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_2, quantity=4)
        chair_AS_3 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_3, quantity=4)
        chairAtomicSpec = [chair_AS_1, chair_AS_2, chair_AS_3]
        for spec in chairAtomicSpec:
            chairBuild.atomic_specifications.add(spec)
        chairBuild.save()

        # define table-set
        self.tablesetBuildprint = Blueprint.objects.create(name="tableset")
        tablesetAtomicPrereq = AtomicPrerequisite.objects.create(atomic_component=self.manual, min_quantity=1,
                                                                 max_quantity=1)
        tableSet_BP_1 = BuildPrerequisite.objects.create(build=tableBuild, min_quantity=1, max_quantity=1)
        tableSet_BP_2 = BuildPrerequisite.objects.create(build=chairBuild, min_quantity=1, max_quantity=4)
        tablesetBuildPrereq = [tableSet_BP_1, tableSet_BP_2]
        self.tablesetBuildprint.atomic_prerequisites.add(tablesetAtomicPrereq)
        for bpReq in tablesetBuildPrereq:
            self.tablesetBuildprint.build_prerequisites.add(bpReq)
        self.tablesetBuildprint.save()

        # Build table-set
        self.tablesetBuild = Build.objects.create(name="tableSet", blueprint=self.tablesetBuildprint)
        tableset_BS_1 = BuildSpecification.objects.create(build_prereq=tableSet_BP_1, quantity=1)
        tableset_BS_2 = BuildSpecification.objects.create(build_prereq=tableSet_BP_2, quantity=4)
        tablesetBuildSpec = [tableset_BS_1, tableset_BS_2]
        for spec in tablesetBuildSpec:
            self.tablesetBuild.build_specifications.add(spec)
        self.tablesetBuild.save()

        # create a list of all requirements
        self.allBuildPrereq = tablesetBuildPrereq

    def test(self):
        """
        Test recursive collection of all AtomicRequirements of a Blueprint
        :return:
        """
        self.assertEqual(set(self.tablesetBuildprint.allBuildPrerequisites()), set(self.allBuildPrereq))

class Blueprint_simple_map_prerequisites(TestCase):
    """
    Single layer blueprint mapping
    """
    def setUp(self):
        # Atomic
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)

        # Define table
        self.tableBlueprint = Blueprint.objects.create(name="table")
        self.table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
        self.table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        self.table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        tableAtomicPrereq = [self.table_AP_1, self.table_AP_2, self.table_AP_3]
        for req in tableAtomicPrereq:
            self.tableBlueprint.atomic_prerequisites.add(req)
        self.tableBlueprint.save()

    def test(self):
        struct = {}
        struct['name'] = "table"
        struct['atomic_prereq'] = [self.table_AP_1, self.table_AP_2, self.table_AP_3]
        struct['build_prereq'] = []
        self.assertDictEqual(self.tableBlueprint.map_prerequisites(), struct)

class Blueprint_map_prerequisites_recursively(TestCase):
    """
    Map prerequisites recursively for blueprint
    """

    def setUp(self):

        # Atomic
        self.manual = AtomicComponent.objects.create(stock_code="man", availability=5)
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)
        self.backplate = AtomicComponent.objects.create(stock_code="backplate", availability=15)

        # Define table
        tableBlueprint = Blueprint.objects.create(name="table")
        table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
        table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        self.tableAtomicPrereq = [table_AP_1, table_AP_2, table_AP_3]
        for req in self.tableAtomicPrereq:
            tableBlueprint.atomic_prerequisites.add(req)
        tableBlueprint.save()

        # Build table
        tableBuild = Build.objects.create(name='table', blueprint=tableBlueprint)
        table_AS_1 = AtomicSpecification.objects.create(atomic_prereq=table_AP_1, quantity=1)
        table_AS_2 = AtomicSpecification.objects.create(atomic_prereq=table_AP_2, quantity=4)
        table_AS_3 = AtomicSpecification.objects.create(atomic_prereq=table_AP_3, quantity=4)
        tableBuildSpec = [table_AS_1, table_AS_2, table_AS_3]
        for spec in tableBuildSpec:
            tableBuild.atomic_specifications.add(spec)
        tableBuild.save()

        # Define chair
        chairBlueprint = Blueprint.objects.create(name="chair")
        chair_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.backplate, min_quantity=1, max_quantity=1)
        chair_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        chair_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        self.chairAtomicPrereq = [chair_AP_1, chair_AP_2, chair_AP_3]
        for prereq in self.chairAtomicPrereq:
            chairBlueprint.atomic_prerequisites.add(prereq)
        chairBlueprint.save()

        # Build chair
        chairBuild = Build.objects.create(name="chair", blueprint=chairBlueprint)
        chair_AS_1 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_1, quantity=1)
        chair_AS_2 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_2, quantity=4)
        chair_AS_3 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_3, quantity=4)
        chairAtomicSpec = [chair_AS_1, chair_AS_2, chair_AS_3]
        for spec in chairAtomicSpec:
            chairBuild.atomic_specifications.add(spec)
        chairBuild.save()

        # define table-set
        self.tablesetBuildprint = Blueprint.objects.create(name="tableset")
        self.tablesetAtomicPrereq = AtomicPrerequisite.objects.create(atomic_component=self.manual, min_quantity=1,
                                                                 max_quantity=1)
        tableSet_BP_1 = BuildPrerequisite.objects.create(build=tableBuild, min_quantity=1, max_quantity=1)
        tableSet_BP_2 = BuildPrerequisite.objects.create(build=chairBuild, min_quantity=1, max_quantity=4)
        tablesetBuildPrereq = [tableSet_BP_1, tableSet_BP_2]
        self.tablesetBuildprint.atomic_prerequisites.add(self.tablesetAtomicPrereq)
        for bpReq in tablesetBuildPrereq:
            self.tablesetBuildprint.build_prerequisites.add(bpReq)
        self.tablesetBuildprint.save()

        # Build table-set
        self.tablesetBuild = Build.objects.create(name="tableSet", blueprint=self.tablesetBuildprint)
        tableset_BS_1 = BuildSpecification.objects.create(build_prereq=tableSet_BP_1, quantity=1)
        tableset_BS_2 = BuildSpecification.objects.create(build_prereq=tableSet_BP_2, quantity=4)
        tablesetBuildSpec = [tableset_BS_1, tableset_BS_2]
        for spec in tablesetBuildSpec:
            self.tablesetBuild.build_specifications.add(spec)
        self.tablesetBuild.save()

        # create a list of all requirements
        self.allBuildPrereq = tablesetBuildPrereq

    def test(self):
        """
        Test recursive collection of all AtomicRequirements of a Blueprint
        :return:
        """
        full_mapping = {
            'name': 'tableset',
            'atomic_prereq': [self.tablesetAtomicPrereq],
            'build_prereq':[
                {
                    'name': 'table',
                    'atomic_prereq': self.tableAtomicPrereq,
                    'build_prereq': []
                },
                {
                    'name': 'chair',
                    'atomic_prereq': self.chairAtomicPrereq,
                    'build_prereq': []
                }
            ]
        }
        self.maxDiff = None
        self.assertDictEqual(self.tablesetBuildprint.map_prerequisites(), full_mapping)

class Build_auditing(TestCase):
    def setUp(self):
        # Atomic
        self.manual = AtomicComponent.objects.create(stock_code="man", availability=5)
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)
        self.backplate = AtomicComponent.objects.create(stock_code="backplate", availability=15)

        # Define table
        tableBlueprint = Blueprint.objects.create(name="table")
        table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
        table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        self.tableAtomicPrereq = [table_AP_1, table_AP_2, table_AP_3]
        for req in self.tableAtomicPrereq:
            tableBlueprint.atomic_prerequisites.add(req)
        tableBlueprint.save()

        # Build table
        self.tableBuild = Build.objects.create(name='table', blueprint=tableBlueprint)
        table_AS_1 = AtomicSpecification.objects.create(atomic_prereq=table_AP_1, quantity=1)
        table_AS_2 = AtomicSpecification.objects.create(atomic_prereq=table_AP_2, quantity=4)
        table_AS_3 = AtomicSpecification.objects.create(atomic_prereq=table_AP_3, quantity=4)
        tableBuildSpec = [table_AS_1, table_AS_2, table_AS_3]
        for spec in tableBuildSpec:
            self.tableBuild.atomic_specifications.add(spec)
        self.tableBuild.save()

    def test(self):
        self.assertTrue(self.tableBuild.prerequisiteAudit().fulfilled())

class Build_map(TestCase):

    def setUp(self):

        # Atomic
        self.manual = AtomicComponent.objects.create(stock_code="man", availability=5)
        self.tabletop = AtomicComponent.objects.create(stock_code="tabletop", availability=20)
        self.leg = AtomicComponent.objects.create(stock_code="leg", availability=60)
        self.screws = AtomicComponent.objects.create(stock_code="screws", availability=8000)
        self.backplate = AtomicComponent.objects.create(stock_code="backplate", availability=15)

        # Define table
        tableBlueprint = Blueprint.objects.create(name="table")
        table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
        table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        tableAtomicPrereq = [table_AP_1, table_AP_2, table_AP_3]
        for req in tableAtomicPrereq:
            tableBlueprint.atomic_prerequisites.add(req)
        tableBlueprint.save()

        # Build table
        tableBuild = Build.objects.create(name='table', blueprint=tableBlueprint)
        table_AS_1 = AtomicSpecification.objects.create(atomic_prereq=table_AP_1, quantity=1)
        table_AS_2 = AtomicSpecification.objects.create(atomic_prereq=table_AP_2, quantity=4)
        table_AS_3 = AtomicSpecification.objects.create(atomic_prereq=table_AP_3, quantity=4)
        self.tableAtomicSpec = [table_AS_1, table_AS_2, table_AS_3]
        for spec in self.tableAtomicSpec:
            tableBuild.atomic_specifications.add(spec)
        tableBuild.save()

        # Define chair
        chairBlueprint = Blueprint.objects.create(name="chair")
        chair_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.backplate, min_quantity=1, max_quantity=1)
        chair_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
        chair_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
        chairAtomicPrereq = [chair_AP_1, chair_AP_2, chair_AP_3]
        for prereq in chairAtomicPrereq:
            chairBlueprint.atomic_prerequisites.add(prereq)
        chairBlueprint.save()

        # Build chair
        chairBuild = Build.objects.create(name="chair", blueprint=chairBlueprint)
        chair_AS_1 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_1, quantity=1)
        chair_AS_2 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_2, quantity=4)
        chair_AS_3 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_3, quantity=4)
        self.chairAtomicSpec = [chair_AS_1, chair_AS_2, chair_AS_3]
        for spec in self.chairAtomicSpec:
            chairBuild.atomic_specifications.add(spec)
        chairBuild.save()

        # define table-set
        self.tablesetBuildprint = Blueprint.objects.create(name="tableset")
        tablesetAtomicPrereq = AtomicPrerequisite.objects.create(atomic_component=self.manual, min_quantity=1,
                                                                 max_quantity=1)
        tableSet_BP_1 = BuildPrerequisite.objects.create(build=tableBuild, min_quantity=1, max_quantity=1)
        tableSet_BP_2 = BuildPrerequisite.objects.create(build=chairBuild, min_quantity=1, max_quantity=4)
        tablesetBuildPrereq = [tableSet_BP_1, tableSet_BP_2]
        self.tablesetBuildprint.atomic_prerequisites.add(tablesetAtomicPrereq)
        for bpReq in tablesetBuildPrereq:
            self.tablesetBuildprint.build_prerequisites.add(bpReq)
        self.tablesetBuildprint.save()

        # Build table-set
        self.tablesetBuild = Build.objects.create(name="tableSet", blueprint=self.tablesetBuildprint)
        tableset_BS_1 = BuildSpecification.objects.create(build_prereq=tableSet_BP_1, quantity=1)
        tableset_BS_2 = BuildSpecification.objects.create(build_prereq=tableSet_BP_2, quantity=4)
        self.tableset_AS_1 = AtomicSpecification.objects.create(atomic_prereq=tablesetAtomicPrereq, quantity=1)
        tablesetBuildSpec = [tableset_BS_1, tableset_BS_2]
        for spec in tablesetBuildSpec:
            self.tablesetBuild.build_specifications.add(spec)
        self.tablesetBuild.atomic_specifications.add(self.tableset_AS_1)
        self.tablesetBuild.save()

        # create a list of all requirements
        self.allBuildPrereq = tablesetBuildPrereq

    def test(self):
        """
        Test aggregation of all atomic specification recursively under build

        Scenario: Ikea table set

        Table-set contains 1 table (blueprint) and 4 chairs (blueprint)
        and a instruction manual (atomic)

        A table contains 1 table-top, 4 legs, 4 screws
        A chair contains a backplate and 4 legs, 4 screws

        Validate
        """
        struc = {
            'name': 'tableSet',
            'atomic_spec': [self.tableset_AS_1],
            'build_spec': [{
                'name': 'table',
                'atomic_spec': self.tableAtomicSpec,
                'build_spec': [],
                'audit': 'Audit: Deficit-0: Surplus-0'
            },
            {
                'name': 'chair',
                'atomic_spec': self.chairAtomicSpec,
                'build_spec': [],
                'audit': 'Audit: Deficit-0: Surplus-0'
            }],
            'audit': 'Audit: Deficit-0: Surplus-0'
        }
        self.maxDiff = None
        self.assertDictEqual(self.tablesetBuild.map_spec(), struc)