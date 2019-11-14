from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification, AtomicGroup
from shop.assembly.models import Blueprint, Product, ProductPrerequisite, ProductSpecification
from shop.attribute.models import Attribute
from shop.models import URL, OffsetImageURL


def run():

    ####
    # End fitting
    ####
    endfitting_group, created = AtomicGroup.objects.get_or_create(name="demo_group")
    AA1600, created = AtomicComponent.objects.get_or_create(
        stock_code="AA1600",
        category="endfitting",
        description="AA1600"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/AA1600-thumb.png")
    AA1600.thumbnail_images.add(thumb)
    illu, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/AA1600.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    AA1600.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
            url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/AA1600-thumb.png")
    AA1600.description_images.add(demo)
    AA1600.save()

    G2000, created = AtomicComponent.objects.get_or_create(
        stock_code="G2000",
        category="endfitting",
        description="G2000"
    )
    thumb, created = URL.objects.get_or_create(
            url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G%232000-thumb.png")
    G2000.thumbnail_images.add(thumb)
    illu, created = OffsetImageURL.objects.get_or_create(
            url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G%232000.PNG",
            offset_x=0,
            offset_y=0,
            position=0
        )
    G2000.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
            url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G%232000-thumb.png")
    G2000.description_images.add(demo)
    G2000.save()
    endfitting_group.members.add(AA1600,G2000)
    endfitting_group.save()


    ####
    #   Extender
    ####
    M5_13_EXT, created = AtomicComponent.objects.get_or_create(
        stock_code="M5-13-EXT",
        category="extender",
        description="M5-13-EXT"
    )
    thumb, created = URL.objects.get_or_create(
            url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-13-EXT-thumb.png")
    M5_13_EXT.thumbnail_images.add(thumb)
    illu, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-13-EXT.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    M5_13_EXT.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
            url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-13-EXT-thumb.png")
    M5_13_EXT.description_images.add(demo)
    M5_13_EXT.save()

    ###
    # Blueprint
    ###
    SS_6_15, created = Blueprint.objects.get_or_create(name="SS-6-15")
    material_attribute, created = Attribute.objects.get_or_create(key="material", value="Carbon",
                                                                  visibility='online')
    SS_6_15.attribute.add(material_attribute)
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
        atomic_component=M5_13_EXT
    )
    rod_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="rod fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=endfitting_group
    )
    body_fitting, created = AtomicPrerequisite.objects.get_or_create(
        name="body fitting",
        min_quantity=0,
        max_quantity=1,
        atomic_group=endfitting_group
    )
    SS_6_15.atomic_prerequisites.add(stroke)
    SS_6_15.atomic_prerequisites.add(extended_length)
    SS_6_15.atomic_prerequisites.add(force)
    SS_6_15.atomic_prerequisites.add(extender)
    SS_6_15.atomic_prerequisites.add(rod_fitting)
    SS_6_15.atomic_prerequisites.add(body_fitting)
    SS_6_15.save()





