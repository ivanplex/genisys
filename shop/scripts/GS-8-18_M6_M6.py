from shop.atomic.models import AtomicComponent, AtomicPrerequisite
from shop.assembly.models import Blueprint
from shop.group.models import AtomicGroup


def run():

    # GS-8-18 M6 M6 Parts
    blueprint = Blueprint.objects.get_or_create(name="GS-8-18 M6 M6 Parts")[0]
    GS_AP_1 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="ROD08SSHCP/M6-8mm").first(),
        min_quantity=1,
        max_quantity=1
    )
    GS_AP_2 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="TUB08SS").first(),
        min_quantity=1,
        max_quantity=1
    )
    GS_AP_3 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="M8VBLKS6").first(),
        min_quantity=1,
        max_quantity=1
    )
    blueprint.atomic_prerequisites.add(GS_AP_1)
    blueprint.atomic_prerequisites.add(GS_AP_2)
    blueprint.atomic_prerequisites.add(GS_AP_3)
    blueprint.save()

    # M8-18 General Parts
    blueprint = Blueprint.objects.get_or_create(name="M8-18 General Parts")[0]
    M8_AP_1 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="BRGIGUS0810").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_2 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="OR08N1315").first(),
        min_quantity=2,
        max_quantity=2
    )
    M8_AP_3 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="OR107127N90").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_4 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="OUT8IGUS").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_5 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PIS8A").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_6 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PLUN06SS").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_7 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PSEUDONYM RF 1mm").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_8 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="SEAL8163N").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_9 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="IN08S").first(),
        min_quantity=1,
        max_quantity=1
    )
    M8_AP_10 = AtomicPrerequisite.objects.get_or_create(
        atomic_component=AtomicComponent.objects.filter(stock_code="PLUG06A").first(),
        min_quantity=1,
        max_quantity=1
    )
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

