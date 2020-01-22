from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification, AtomicGroup
from shop.assembly.models import Blueprint, BlueprintAttribute
# from shop.attribute.models import Attribute
from shop.models import URL, OffsetImageURL


def SS_6_15():

    SS_6_15, created = Blueprint.objects.get_or_create(name="SS-6-15")
    BlueprintAttribute.objects.get_or_create(blueprint=SS_6_15, key="material", value="Stainless Steel")
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/ModelThumbGeneric.png")
    SS_6_15.thumbnail_image = thumb
    stroke, created = AtomicPrerequisite.objects.get_or_create(
        name="stroke",
        min_quantity=10,
        max_quantity=400,
        virtual=True
    )
    extended_length, created = AtomicPrerequisite.objects.get_or_create(
        name="extended length",
        min_quantity=200,
        max_quantity=1000,
        virtual=True
    )
    force, created = AtomicPrerequisite.objects.get_or_create(
        name="force",
        min_quantity=25,
        max_quantity=400,
        virtual=True
    )
    extender, created = AtomicPrerequisite.objects.get_or_create(
        name="extender",
        min_quantity=0,
        max_quantity=1,
        atomic_component=AtomicComponent.objects.filter(sku="M5-13-EXT").first()
    )
    sleeve, created = AtomicPrerequisite.objects.get_or_create(
        name="sleeve",
        min_quantity=0,
        max_quantity=2,
        atomic_group=AtomicGroup.objects.filter(name="sleeves").first()
    )
    rod_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="rod fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M5-Endfitting").first()
    )
    body_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="body fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M5-Endfitting").first()
    )
    SS_6_15.atomic_prerequisites.add(stroke)
    SS_6_15.atomic_prerequisites.add(extended_length)
    SS_6_15.atomic_prerequisites.add(force)
    SS_6_15.atomic_prerequisites.add(extender)
    SS_6_15.atomic_prerequisites.add(sleeve)
    SS_6_15.atomic_prerequisites.add(rod_fitting)
    SS_6_15.atomic_prerequisites.add(body_fitting)
    SS_6_15.save()


def CS_6_15():

    CS_6_15, created = Blueprint.objects.get_or_create(name="CS-6-15")
    BlueprintAttribute.objects.get_or_create(blueprint=CS_6_15, key="material", value="Carbon")

    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/ModelThumbGeneric.png")
    CS_6_15.thumbnail_image = thumb
    stroke, created = AtomicPrerequisite.objects.get_or_create(
        name="stroke",
        min_quantity=10,
        max_quantity=400,
        virtual=True
    )
    extended_length, created = AtomicPrerequisite.objects.get_or_create(
        name="extended length",
        min_quantity=200,
        max_quantity=1000,
        virtual=True
    )
    force, created = AtomicPrerequisite.objects.get_or_create(
        name="force",
        min_quantity=25,
        max_quantity=400,
        virtual=True
    )
    extender, created = AtomicPrerequisite.objects.get_or_create(
        name="extender",
        min_quantity=0,
        max_quantity=1,
        atomic_component=AtomicComponent.objects.filter(sku="M5-13-EXT").first()
    )
    sleeve, created = AtomicPrerequisite.objects.get_or_create(
        name="sleeve",
        min_quantity=0,
        max_quantity=2,
        atomic_group=AtomicGroup.objects.filter(name="sleeves").first()
    )
    rod_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="rod fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M5-Endfitting").first()
    )
    body_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="body fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M5-Endfitting").first()
    )
    CS_6_15.atomic_prerequisites.add(stroke)
    CS_6_15.atomic_prerequisites.add(extended_length)
    CS_6_15.atomic_prerequisites.add(force)
    CS_6_15.atomic_prerequisites.add(extender)
    CS_6_15.atomic_prerequisites.add(sleeve)
    CS_6_15.atomic_prerequisites.add(rod_fitting)
    CS_6_15.atomic_prerequisites.add(body_fitting)
    CS_6_15.save()


def SS_8_18():

    SS_8_18, created = Blueprint.objects.get_or_create(name="SS-8-18")
    BlueprintAttribute.objects.get_or_create(blueprint=SS_8_18, key="material", value="Stainless Steel")

    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/ModelThumbGeneric.png")
    SS_8_18.thumbnail_image = thumb
    stroke, created = AtomicPrerequisite.objects.get_or_create(
        name="stroke",
        min_quantity=10,
        max_quantity=700,
        virtual=True
    )
    extended_length, created = AtomicPrerequisite.objects.get_or_create(
        name="extended length",
        min_quantity=200,
        max_quantity=1000,
        virtual=True
    )
    force, created = AtomicPrerequisite.objects.get_or_create(
        name="force",
        min_quantity=50,
        max_quantity=750,
        virtual=True
    )
    extender, created = AtomicPrerequisite.objects.get_or_create(
        name="extender",
        min_quantity=0,
        max_quantity=1,
        atomic_component=AtomicComponent.objects.filter(sku="M5-15-EXT").first()
    )
    sleeve, created = AtomicPrerequisite.objects.get_or_create(
        name="sleeve",
        min_quantity=0,
        max_quantity=2,
        atomic_group=AtomicGroup.objects.filter(name="sleeves").first()
    )
    rod_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="rod fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M8-Endfitting").first()
    )
    body_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="body fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M8-Endfitting").first()
    )
    SS_8_18.atomic_prerequisites.add(stroke)
    SS_8_18.atomic_prerequisites.add(extended_length)
    SS_8_18.atomic_prerequisites.add(force)
    SS_8_18.atomic_prerequisites.add(extender)
    SS_8_18.atomic_prerequisites.add(sleeve)
    SS_8_18.atomic_prerequisites.add(rod_fitting)
    SS_8_18.atomic_prerequisites.add(body_fitting)
    SS_8_18.save()


def CS_8_18():

    CS_8_18, created = Blueprint.objects.get_or_create(name="CS-8-18")
    BlueprintAttribute.objects.get_or_create(blueprint=CS_8_18, key="material", value="Carbon")

    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/ModelThumbGeneric.png")
    CS_8_18.thumbnail_image = thumb
    stroke, created = AtomicPrerequisite.objects.get_or_create(
        name="stroke",
        min_quantity=10,
        max_quantity=700,
        virtual=True
    )
    extended_length, created = AtomicPrerequisite.objects.get_or_create(
        name="extended length",
        min_quantity=200,
        max_quantity=1000,
        virtual=True
    )
    force, created = AtomicPrerequisite.objects.get_or_create(
        name="force",
        min_quantity=50,
        max_quantity=750,
        virtual=True
    )
    extender, created = AtomicPrerequisite.objects.get_or_create(
        name="extender",
        min_quantity=0,
        max_quantity=1,
        atomic_component=AtomicComponent.objects.filter(sku="M5-15-EXT").first()
    )
    sleeve, created = AtomicPrerequisite.objects.get_or_create(
        name="sleeve",
        min_quantity=0,
        max_quantity=2,
        atomic_group=AtomicGroup.objects.filter(name="sleeves").first()
    )
    rod_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="rod fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M8-Endfitting").first()
    )
    body_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="body fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=AtomicGroup.objects.filter(name="M8-Endfitting").first()
    )
    CS_8_18.atomic_prerequisites.add(stroke)
    CS_8_18.atomic_prerequisites.add(extended_length)
    CS_8_18.atomic_prerequisites.add(force)
    CS_8_18.atomic_prerequisites.add(extender)
    CS_8_18.atomic_prerequisites.add(sleeve)
    CS_8_18.atomic_prerequisites.add(rod_fitting)
    CS_8_18.atomic_prerequisites.add(body_fitting)
    CS_8_18.save()

def run():

    SS_6_15()
    SS_8_18()
    CS_6_15()
    CS_8_18()
