from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification, AtomicGroup
from shop.assembly.models import Blueprint, Product, ProductPrerequisite, ProductSpecification


def run():
    # GS-8-18 M6 M6 Parts
    print("GS-8-18 M6 M6 Parts:")
    print("     - create blueprint GS-8-18 M6 M6 Parts")
    blueprint = Blueprint.objects.get_or_create(name="GS-8-18 M6 M6 Parts")[0]
    print("     - import prerequisite for GS-8-18 M6 M6 Parts")
    GS_AP_1 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="ROD08SSHCP/M6-8mm").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    GS_AP_2 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="TUB08SS").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    GS_AP_3 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="M8VBLKS6").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    blueprint.atomic_prerequisites.add(GS_AP_1)
    blueprint.atomic_prerequisites.add(GS_AP_2)
    blueprint.atomic_prerequisites.add(GS_AP_3)
    blueprint.save()

    print("     - create product GS-8-18 M6 M6 Parts")
    GS_product = Product.objects.get_or_create(name="GS-8-18 M6 M6 Parts", blueprint=blueprint)[0]
    print("     - add product specifications for GS-8-18 M6 M6 Parts")
    GS_AS_1 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="ROD08SSHCP/M6-8mm").first(),
        atomic_prereq=GS_AP_1,
        quantity=1
    )[0]
    GS_AS_2 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="TUB08SS").first(),
        atomic_prereq=GS_AP_2,
        quantity=1
    )[0]
    GS_AS_3 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="M8VBLKS6").first(),
        atomic_prereq=GS_AP_3,
        quantity=1
    )[0]
    GS_product.atomic_specifications.add(GS_AS_1)
    GS_product.atomic_specifications.add(GS_AS_2)
    GS_product.atomic_specifications.add(GS_AS_3)
    GS_product.save()


    # M8-18 General Parts
    print("M8-18 General Parts")
    print("     - create blueprint M8-18 General Parts")
    blueprint = Blueprint.objects.get_or_create(name="M8-18 General Parts")[0]
    print("     - import prerequisite for M8-18 General Parts")
    M8_AP_1 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="BRGIGUS0810").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_2 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="OR08N1315").first(),
        min_quantity=2,
        max_quantity=2
    )[0]
    M8_AP_3 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="OR107127N90").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_4 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="OUT8IGUS").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_5 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PIS8A").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_6 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PLUN06SS").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_7 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PSEUDONYM RF 1mm").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_8 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="SEAL8163N").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_9 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="IN08S").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    M8_AP_10 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PLUG06A").first(),
        min_quantity=1,
        max_quantity=1
    )[0]
    blueprint.atomic_prerequisites.add(M8_AP_1)
    blueprint.atomic_prerequisites.add(M8_AP_2)
    blueprint.atomic_prerequisites.add(M8_AP_3)
    blueprint.atomic_prerequisites.add(M8_AP_4)
    blueprint.atomic_prerequisites.add(M8_AP_5)
    blueprint.atomic_prerequisites.add(M8_AP_6)
    blueprint.atomic_prerequisites.add(M8_AP_7)
    blueprint.atomic_prerequisites.add(M8_AP_8)
    blueprint.atomic_prerequisites.add(M8_AP_9)
    blueprint.atomic_prerequisites.add(M8_AP_10)
    blueprint.save()

    print("     - create product M8-18 General Parts")
    M8_product = Product.objects.get_or_create(name="M8-18 General Parts", blueprint=blueprint)[0]
    print("     - add specifications for M8-18 General Parts")
    M8_AS_1 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="BRGIGUS0810").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_2 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="OR08N1315").first(),
        atomic_prereq=M8_AP_1,
        quantity=2
    )[0]
    M8_AS_3 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="OR107127N90").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_4 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="OUT8IGUS").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_5 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="PIS8A").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_6 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="PLUN06SS").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_7 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="PSEUDONYM RF 1mm").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_8 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="SEAL8163N").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_9 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="IN08S").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_AS_10 = AtomicSpecification.objects.get_or_create(
        selected_component=AtomicComponent.objects.filter(stock_code="PLUG06A").first(),
        atomic_prereq=M8_AP_1,
        quantity=1
    )[0]
    M8_product.atomic_specifications.add(M8_AS_1)
    M8_product.atomic_specifications.add(M8_AS_2)
    M8_product.atomic_specifications.add(M8_AS_3)
    M8_product.atomic_specifications.add(M8_AS_4)
    M8_product.atomic_specifications.add(M8_AS_5)
    M8_product.atomic_specifications.add(M8_AS_6)
    M8_product.atomic_specifications.add(M8_AS_7)
    M8_product.atomic_specifications.add(M8_AS_8)
    M8_product.atomic_specifications.add(M8_AS_9)
    M8_product.atomic_specifications.add(M8_AS_10)
    M8_product.save()

    # GS-8-18 M6 M6
    print("GS-8-18 M6 M6: ")
    print("     - create blueprint GS-8-18 M6 M6")
    blueprint = Blueprint.objects.get_or_create(name="GS-8-18 M6 M6")[0]
    print("     - add product prerequisites for GS-8-18 M6 M6")
    PP_1 = ProductPrerequisite.objects.get_or_create(product=GS_product, min_quantity=1, max_quantity=1)[0]
    PP_2 = ProductPrerequisite.objects.get_or_create(product=M8_product, min_quantity=1, max_quantity=1)[0]
    blueprint.product_prerequisites.add(PP_1)
    blueprint.product_prerequisites.add(PP_2)
    blueprint.save()

    print("     - create M8 endfitting group")
    M8_EF_group = AtomicGroup.objects.get_or_create(
        name='M8 Endfittings',
        description='All endfittings for M8'
    )[0]
    print("     - populate M8 endfitting group")
    valid_endfittings = ["Ball Cup WCS1800", "Ball Joint ADKG M8", "Ball Joint PLS4M8", "Ball Joint WCS2500", "Ball Joint WE1801", "Ball Joint WE1900", "Ball Joint WE2500", "Ball Joint WE3000", "Ball Joint WN2001", "Ball Joint WN2501", "Ball Joint WN3001", "Ball Joint WN3002", "Ball Joint WS2000", "Ball Joint WS2300", "Ball Joint WS2500", "Ball Joint WS3000", "Ball Joint WS3000A", "Ball Joint WY2000", "Ball Joint WY3000", "Cutdown Rose Joints ASPE3600 - 32mm CF", "Eye Joint AA1600", "Eye Joint AA1601", "Eye Joint AA3000", "Eye Joint AB15120", "Eye Joint AE1300", "Eye Joint AE15121", "Eye Joint AE1601", "Eye Joint AE1900", "Eye Joint AE1901", "Eye Joint AE1906", "Eye Joint AE2012", "Eye Joint AL2305", "Eye Joint AL2306", "Eye Joint AS1900", "EYE JOINT AS1900 CUT DOWN TO 17", "Eye Joint AS1905", "Eye Joint AS2305", "Eye Joint AS2500", "Eye Joint AS2705", "Eye Joint AS2710", "Fork Joint GE3201", "Fork Joint GE3202", "Fork Joint GS3201", "Fork Joint GS4800", "None M8", "Rose Joints ASPE3600", "Rose Joints ASPS3600", "Rose Joints ASPY3600", "WS3000 - 2.5mm cut down"]
    for endfittings in valid_endfittings:
        atom = AtomicComponent.objects.filter(description=endfittings).first()
        if atom:
            M8_EF_group.members.add(atom)
    M8_EF_group.save()
    print("     - add endfitting prerequisite for GS-8-18 M6 M6")
    AP_1 = AtomicPrerequisite.objects.get_or_create(name="Left End-fitting", atomic_group=M8_EF_group,
                                                    min_quantity=0, max_quantity=1)[0]
    AP_2 = AtomicPrerequisite.objects.get_or_create(name="Right End-fitting", atomic_group=M8_EF_group,
                                                    min_quantity=0, max_quantity=1)[0]
    blueprint.atomic_prerequisites.add(AP_1)
    blueprint.atomic_prerequisites.add(AP_2)
    blueprint.save()

    product, created = Product.objects.get_or_create(name="GS-8-18 M6 M6",
                                            sku="GS-8-18 M6 M6",
                                            availability=1,
                                            blueprint=blueprint)
    AS_1, created = AtomicSpecification.objects.get_or_create(name="Left End-fitting",
                                                     selected_component=AtomicComponent.objects.filter(description="Ball Joint PLS4M8").first(),
                                                     atomic_prereq=AP_1,
                                                     quantity=1)
    AS_2, created = AtomicSpecification.objects.get_or_create(name="Right End-fitting",
                                                     selected_component=AtomicComponent.objects.filter(
                                                         description="Ball Joint PLS4M8").first(),
                                                     atomic_prereq=AP_2,
                                                     quantity=1)
    product.atomic_specifications.add(AS_1)
    product.atomic_specifications.add(AS_2)
    PS_1, created = ProductSpecification.objects.get_or_create(name="GS-8-18 M6 M6 Parts",
                                                               selected_component=GS_product,
                                                               product_prereq=PP_1,
                                                               quantity=1)
    PS_2, created = ProductSpecification.objects.get_or_create(name="M8-18 General Parts",
                                                               selected_component=M8_product,
                                                               product_prereq=PP_2,
                                                               quantity=1)
    product.product_specifications.add(PS_1)
    product.product_specifications.add(PS_2)
    product.save()





