from django.test import TestCase
from modular_assembly.assembly.models import Blueprint, ProductPrerequisite, Product, ProductSpecification
from modular_assembly.atomic.models import AtomicPrerequisite, AtomicSpecification, AtomicComponent


class BlueprintAssignMultipleAtomicTestCase(TestCase):
    def test(self):
        """
        Test assign multiple atomicComponent
        """

        component = [
            AtomicComponent.objects.create(sku="Apple", availability=700),
            AtomicComponent.objects.create(sku="Orange", availability=400),
            AtomicComponent.objects.create(sku="Banana", availability=200)
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


class BlueprintAssignBlueprintTestCase(TestCase):
    def test(self):
        """
        Test assigning blueprint requirement on blueprint
        """
        try:
            # define
            a = AtomicComponent.objects.create(sku="TEST", availability=700)
            ar = AtomicPrerequisite.objects.create(atomic_component=a, min_quantity=4, max_quantity=4)
            b = Blueprint.objects.create(name="Table")
            b.atomic_prerequisites.add(ar)
            b.save()

            # build
            tableBuild = Product.objects.create(name="table", blueprint=b)
            tableBuildAtomicSpec = AtomicSpecification.objects.create(selected_component=a, prerequisite=ar, quantity=4)
            tableBuild.atomic_specifications.add(tableBuildAtomicSpec)

            b_set = Blueprint.objects.create(name="Table_set")
            b_set_req = ProductPrerequisite.objects.create(product=tableBuild, min_quantity=2, max_quantity=2)
            b_set.product_prerequisites.add(b_set_req)
            b_set.save()
        except:
            self.fail('Creation of Blueprint object failed.')


class BlueprintEmptinessTestCase(TestCase):

    def setUp(self):
        # atomic
        atom = AtomicComponent.objects.create(sku='U-Bolt', availability=300)

        # define table
        self.table = Blueprint.objects.create(name='table')

    def test_true_empty(self):
        """
        True empty of a Blueprint
        """
        self.assertEqual(self.table.isEmpty(), True)

    def test_false_empty(self):
        """
        False empty when blueprint contains atomicComponent
        """
        self.r = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(sku='U-Bolt', availability=300), min_quantity=2,
            max_quantity=2)
        self.table.atomic_prerequisites.add(self.r)
        self.table.save()
        self.assertEqual(self.table.isEmpty(), False)

    def test_child_false_empty(self):
        """
        False empty when child of a blueprint contains atomicPrereq
        """
        self.a = AtomicComponent.objects.create(sku='U-Bolt', availability=300)
        self.r = AtomicPrerequisite.objects.create(
            atomic_component=self.a, min_quantity=2,
            max_quantity=2)
        self.table.atomic_prerequisites.add(self.r)
        self.table.save()

        # build table
        tableBuild = Product.objects.create(name="table", blueprint=self.table)
        tableAtomicSpec = AtomicSpecification.objects.create(
            selected_component=self.a, prerequisite=self.r, quantity=2)
        tableBuild.atomic_specifications.add(tableAtomicSpec)
        tableBuild.save()

        br = ProductPrerequisite.objects.create(product=tableBuild, min_quantity=1, max_quantity=1)

        # define table-set
        self.tableset = Blueprint.objects.create(name='tableSet')
        tablesetBuildPrereq = ProductPrerequisite.objects.create(product=tableBuild, min_quantity=1, max_quantity=1)
        self.tableset.product_prerequisites.add(tablesetBuildPrereq)
        self.tableset.save()

        self.assertEqual(self.tableset.isEmpty(), False)


# class IkeaTableSetTestCase(TestCase):
#     """
#     Scenario: Ikea table set
#
#     Table-set contains 1 table (blueprint) and 4 chairs (blueprint)
#     and a instruction manual (atomic)
#
#     A table contains 1 table-top, 4 legs, 4 screws
#     A chair contains a backplate and 4 legs, 4 screws
#     """
#     def setUp(self):
#         # Atomic
#         self.manual = AtomicComponent.objects.create(sku="man", availability=5)
#         self.tabletop = AtomicComponent.objects.create(sku="tabletop", availability=20)
#         self.leg = AtomicComponent.objects.create(sku="leg", availability=60)
#         self.screws = AtomicComponent.objects.create(sku="screws", availability=8000)
#         self.backplate = AtomicComponent.objects.create(sku="backplate", availability=15)
#
#         # Define table
#         self.tableBlueprint = Blueprint.objects.create(name="table")
#         table_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.tabletop, min_quantity=1, max_quantity=1)
#         table_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
#         table_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
#         self.tableAtomicPrereq = [table_AP_1, table_AP_2, table_AP_3]
#         for req in self.tableAtomicPrereq:
#             self.tableBlueprint.atomic_prerequisites.add(req)
#         self.tableBlueprint.save()
#
#         # Build table
#         self.tableBuild = Product.objects.create(name='table', blueprint=self.tableBlueprint)
#         table_AS_1 = AtomicSpecification.objects.create(atomic_prereq=table_AP_1, quantity=1)
#         table_AS_2 = AtomicSpecification.objects.create(atomic_prereq=table_AP_2, quantity=4)
#         table_AS_3 = AtomicSpecification.objects.create(atomic_prereq=table_AP_3, quantity=4)
#         self.tableAtomicSpec = [table_AS_1, table_AS_2, table_AS_3]
#         for spec in self.tableAtomicSpec:
#             self.tableBuild.atomic_specifications.add(spec)
#         self.tableBuild.save()
#
#         # Define chair
#         chairBlueprint = Blueprint.objects.create(name="chair")
#         chair_AP_1 = AtomicPrerequisite.objects.create(atomic_component=self.backplate, min_quantity=1, max_quantity=1)
#         chair_AP_2 = AtomicPrerequisite.objects.create(atomic_component=self.leg, min_quantity=4, max_quantity=4)
#         chair_AP_3 = AtomicPrerequisite.objects.create(atomic_component=self.screws, min_quantity=4, max_quantity=4)
#         self.chairAtomicPrereq = [chair_AP_1, chair_AP_2, chair_AP_3]
#         for prereq in self.chairAtomicPrereq:
#             chairBlueprint.atomic_prerequisites.add(prereq)
#         chairBlueprint.save()
#
#         # Build chair
#         self.chairBuild = Product.objects.create(name="chair", blueprint=chairBlueprint)
#         chair_AS_1 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_1, quantity=1)
#         chair_AS_2 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_2, quantity=4)
#         chair_AS_3 = AtomicSpecification.objects.create(atomic_prereq=chair_AP_3, quantity=4)
#         self.chairAtomicSpec = [chair_AS_1, chair_AS_2, chair_AS_3]
#         for spec in self.chairAtomicSpec:
#             self.chairBuild.atomic_specifications.add(spec)
#         self.chairBuild.save()
#
#         # define table-set
#         self.tablesetBuildprint = Blueprint.objects.create(name="tableset")
#         self.tablesetAtomicPrereq = AtomicPrerequisite.objects.create(atomic_component=self.manual, min_quantity=1,
#                                                                  max_quantity=1)
#         tableSet_BP_1 = ProductPrerequisite.objects.create(product=self.tableBuild, min_quantity=1, max_quantity=1)
#         tableSet_BP_2 = ProductPrerequisite.objects.create(product=self.chairBuild, min_quantity=1, max_quantity=4)
#         self.tablesetBuildPrereq = [tableSet_BP_1, tableSet_BP_2]
#         self.tablesetBuildprint.atomic_prerequisites.add(self.tablesetAtomicPrereq)
#         for bpReq in self.tablesetBuildPrereq:
#             self.tablesetBuildprint.product_prerequisites.add(bpReq)
#         self.tablesetBuildprint.save()
#
#         # Build table-set
#         self.tablesetBuild = Product.objects.create(name="tableSet", blueprint=self.tablesetBuildprint)
#         tableset_BS_1 = ProductSpecification.objects.create(product_prereq=tableSet_BP_1, quantity=1)
#         tableset_BS_2 = ProductSpecification.objects.create(product_prereq=tableSet_BP_2, quantity=4)
#         self.tableset_AS_1 = AtomicSpecification.objects.create(atomic_prereq=self.tablesetAtomicPrereq, quantity=1)
#         tablesetBuildSpec = [tableset_BS_1, tableset_BS_2]
#         for spec in tablesetBuildSpec:
#             self.tablesetBuild.product_specifications.add(spec)
#         self.tablesetBuild.atomic_specifications.add(self.tableset_AS_1)
#         self.tablesetBuild.save()
#
#     def test_agg_blueprint_atomic_prerequisite(self):
#         """
#         Test aggregation of all atomic prerequisite recursively under blueprint
#         """
#         # create a list of all requirements
#         self.allAtomicRequirements = self.tableAtomicPrereq + self.chairAtomicPrereq + [self.tablesetAtomicPrereq]
#
#         self.assertEqual(set(self.tablesetBuildprint.allAtomicPrerequisites()), set(self.allAtomicRequirements))
#
#
