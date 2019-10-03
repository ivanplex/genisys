from django.test import TestCase
from shop.atomic.models import AtomicComponent, AtomicSpecification, AtomicPrerequisite
from shop.assembly.models import PrerequisiteAudit, Blueprint, Product, ProductPrerequisite, ProductSpecification


class PrerequisiteAuditTestCase(TestCase):

    def test_fulfilled(self):
        audit = PrerequisiteAudit()
        self.assertTrue(audit.fulfilled())

    def test_deficit(self):
        audit = PrerequisiteAudit()
        audit.deficit.append(1)
        self.assertFalse(audit.fulfilled())

    def test_surplus(self):
        audit = PrerequisiteAudit()
        audit.surplus.append(1)
        self.assertFalse(audit.fulfilled())

    def test_deficit_and_surplus(self):
        audit = PrerequisiteAudit()
        audit.deficit.append(1)
        audit.surplus.append(1)
        self.assertFalse(audit.fulfilled())


class ProductHasPrerequisite(TestCase):
    def setUp(self):
        self.b2_blueprint = Blueprint.objects.create(name="LowerBlueprint")
        self.b2 = Product.objects.create(name="LowerBuild", blueprint=self.b2_blueprint)

    def test_True(self):
        """
        Test if Product has prerequisite
        """
        b1_blueprint = Blueprint.objects.create(name="UpperBlueprint")
        b1_product_prerequisite = ProductPrerequisite.objects.create(product=self.b2, min_quantity=1, max_quantity=1)
        b1_blueprint.product_prerequisites.add(b1_product_prerequisite)

        self.b1 = Product.objects.create(name="UpperBuild", blueprint=b1_blueprint)
        self.assertTrue(self.b1.hasProductPrerequisite())

    def test_False(self):
        """
        Test if Product has no prerequisite
        """
        self.assertFalse(self.b2.hasProductPrerequisite())


class ProductAuditPrerequisiteTestCase(TestCase):

    def setUp(self):
        self.blueprint = Blueprint.objects.create(name="Table")
        self.atomic_prerequisite = [
            AtomicPrerequisite.objects.create(
                atomic_component=AtomicComponent.objects.create(stock_code='U-Bolt', availability=300),
                min_quantity=4, max_quantity=8),
            AtomicPrerequisite.objects.create(
                atomic_component=AtomicComponent.objects.create(stock_code='T-Bolt', availability=300),
                min_quantity=4, max_quantity=8)
        ]

        for prerequisite in self.atomic_prerequisite:
            self.blueprint.atomic_prerequisites.add(prerequisite)
        self.blueprint.save()

    def test_comply(self):
        """
        Test 2 atomic prerequisite being followed by atomic specification
        accordingly
        """
        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite[1], quantity=20)
        ]
        for spec in self.atomic_specs:
            self.product.atomic_specifications.add(spec)
        self.product.save()

        self.assertTrue(self.product.prerequisiteAudit().fulfilled())

    def test_compliance_deficit(self):
        """
        Test missing atomic specification
        One of the AtomicPrerequisite has not been followed by specification
        """
        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite[0], quantity=6),
        ]
        for spec in self.atomic_specs:
            self.product.atomic_specifications.add(spec)
        self.product.save()

        self.assertFalse(self.product.prerequisiteAudit().fulfilled())

    def test_compliance_surplus(self):
        """
        Test additional atomic specification
        One unknown specification exist
        """
        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)

        self.additional_pre = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='C-Bolt', availability=300),
            min_quantity=4, max_quantity=8)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite[1], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.additional_pre, quantity=6)
        ]
        for spec in self.atomic_specs:
            self.product.atomic_specifications.add(spec)
        self.product.save()

        self.assertFalse(self.product.prerequisiteAudit().fulfilled())

    def test_compliance_deficit_and_surplus(self):
        """
        One specification is missing and unknown specification found
        """
        self.product = Product.objects.create(name='Table', blueprint=self.blueprint)

        self.additional_pre = AtomicPrerequisite.objects.create(
            atomic_component=AtomicComponent.objects.create(stock_code='C-Bolt', availability=300),
            min_quantity=4, max_quantity=8)

        self.atomic_specs = [
            AtomicSpecification.objects.create(atomic_prereq=self.atomic_prerequisite[0], quantity=6),
            AtomicSpecification.objects.create(atomic_prereq=self.additional_pre, quantity=6)
        ]
        for spec in self.atomic_specs:
            self.product.atomic_specifications.add(spec)
        self.product.save()

        self.assertFalse(self.product.prerequisiteAudit().fulfilled())


class Build_Audit_prerequisite_recursive(TestCase):
    def setUp(self):

        # Define atomic variables
        a_table_top = AtomicComponent.objects.create(stock_code='Table-Top', availability=50)
        a_table_leg = AtomicComponent.objects.create(stock_code='Table-leg', availability=700)
        a_chair = AtomicComponent.objects.create(stock_code='chair', availability=300)

        # define table
        table_blueprint = Blueprint.objects.create(name="Table")

        ap_table_top = AtomicPrerequisite.objects.create(atomic_component=a_table_top, min_quantity=1, max_quantity=1)
        ap_table_leg = AtomicPrerequisite.objects.create(atomic_component=a_table_leg, min_quantity=4, max_quantity=8)
        table_atomic_prereqs = [ap_table_top, ap_table_leg]

        for prerequisite in table_atomic_prereqs:
            table_blueprint.atomic_prerequisites.add(prerequisite)
        table_blueprint.save()

        # Build table
        tableBuild = Product.objects.create(name='Table', blueprint=table_blueprint)
        AS_table_top = AtomicSpecification.objects.create(atomic_prereq=ap_table_top, quantity=1)
        AS_table_leg = AtomicSpecification.objects.create(atomic_prereq=ap_table_leg, quantity=4)
        tableBuild_atomic_spec = [AS_table_top, AS_table_leg]
        for spec in tableBuild_atomic_spec:
            tableBuild.atomic_specifications.add(spec)
        tableBuild.save()

        # define table-set
        tableSetBlueprint = Blueprint.objects.create(name="tableSet")
        tableSetBuildPrereq = ProductPrerequisite.objects.create(
            product=tableBuild, min_quantity=1, max_quantity=1)
        tableSetAtomicPrereq = AtomicPrerequisite.objects.create(
            atomic_component=a_chair, min_quantity=2, max_quantity=4)
        tableSetBlueprint.product_prerequisites.add(tableSetBuildPrereq)
        tableSetBlueprint.atomic_prerequisites.add(tableSetAtomicPrereq)
        tableSetBlueprint.save()

        # build table-set
        self.tableSetBuild = Product.objects.create(name='TableSet', blueprint=tableSetBlueprint)
        AS_tableset_chairs = AtomicSpecification.objects.create(atomic_prereq=tableSetAtomicPrereq, quantity=4)
        self.tableSetBuild.atomic_specifications.add(AS_tableset_chairs)

        self.tableSetBuild.product_specifications.add(
            ProductSpecification.objects.create(product_prereq=tableSetBuildPrereq, quantity=1)
        )
        self.tableSetBuild.save()

    def test(self):
        self.assertEqual(self.tableSetBuild.prerequisiteAudit().fulfilled(), True)
