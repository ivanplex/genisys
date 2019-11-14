from shop.atomic.models import AtomicComponent, AtomicGroup
from shop.models import URL, OffsetImageURL




def createEndfitting():

    # AA1600
    AA1600, created = AtomicComponent.objects.get_or_create(
        stock_code="AA1600",
        category="endfitting",
        description="AA1600"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/AA1600-thumb.png")
    AA1600.thumbnail_image = thumb
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

    # G2000
    G2000, created = AtomicComponent.objects.get_or_create(
        stock_code="G2000",
        category="endfitting",
        description="G2000"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G%232000-thumb.png")
    G2000.thumbnail_image = thumb
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

    # M5
    M5, created = AtomicComponent.objects.get_or_create(
        stock_code="M5",
        category="endfitting",
        description="M5"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-Thread-thumb.png")
    M5.thumbnail_image = thumb
    illu, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-Thread.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    M5.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-Thread-thumb.png")
    M5.description_images.add(demo)
    M5.save()

    # WS3000
    WS3000, created = AtomicComponent.objects.get_or_create(
        stock_code="WS3000",
        category="endfitting",
        description="WS3000"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/W-3000 - thumb.png")
    WS3000.thumbnail_image = thumb
    illu, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/W-3000.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    WS3000.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/W-3000 - thumb.png")
    WS3000.description_images.add(demo)
    WS3000.save()

    M5_Endfitting_group, created = AtomicGroup.objects.get_or_create(name="M5-Endfitting")
    M5_Endfitting_group.members.add(AA1600, G2000, M5)
    M5_Endfitting_group.save()

    M8_Endfitting_group, created = AtomicGroup.objects.get_or_create(name="M8-Endfitting")
    M8_Endfitting_group.members.add(WS3000)
    M8_Endfitting_group.save()


def createExtender():

    # M5_13_EXT
    M5_13_EXT, created = AtomicComponent.objects.get_or_create(
        stock_code="M5-13-EXT",
        category="extender",
        description="M5-13-EXT"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-13-EXT-thumb.png")
    M5_13_EXT.thumbnail_image = thumb
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

    # M5_15_EXT
    M5_15_EXT, created = AtomicComponent.objects.get_or_create(
        stock_code="M5-15-EXT",
        category="extender",
        description="M5-15-EXT"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-15-EXT-thumb.png")
    M5_15_EXT.thumbnail_image = thumb
    illu, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-15-EXT.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    M5_15_EXT.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M5-15-EXT-thumb.png")
    M5_15_EXT.description_images.add(demo)
    M5_15_EXT.save()

    # M8_20_EXT
    M8_20_EXT, created = AtomicComponent.objects.get_or_create(
        stock_code="M8-20-EXT",
        category="extender",
        description="M8-20-EXT"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M8-20-EXT-thumb.png")
    M8_20_EXT.thumbnail_image = thumb
    illu, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M8-20-EXT.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    M8_20_EXT.illustration_images.add(illu)
    demo, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/M8-20-EXT-thumb.png")
    M8_20_EXT.description_images.add(demo)
    M8_20_EXT.save()

    M5_EXT_GROUP, created = AtomicGroup.objects.get_or_create(name="M5-EXT-GROUP")
    M5_EXT_GROUP.members.add(M5_13_EXT)
    M5_EXT_GROUP.save()

    M8_EXT_GROUP, created = AtomicGroup.objects.get_or_create(name="M8-EXT-GROUP")
    M8_EXT_GROUP.members.add(M5_15_EXT, M8_20_EXT)
    M8_EXT_GROUP.save()


def createSleeves():

    # LO-23
    LO_23, created = AtomicComponent.objects.get_or_create(
        stock_code="LO-23",
        category="open-sleeve",
        description="LO-23 Open Sleeve"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LO-thumb.png")
    LO_23.thumbnail_image = thumb
    illu_left, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LO-Left-Rod.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    LO_23.illustration_images.add(illu_left)
    illu_middle, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LockOpen-Span.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    LO_23.illustration_images.add(illu_middle)
    illu_right, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LO-Right.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    LO_23.illustration_images.add(illu_right)
    demo, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LO-thumb.png")
    LO_23.description_images.add(demo)
    LO_23.save()

    # PS-23
    PS_23, created = AtomicComponent.objects.get_or_create(
        stock_code="PS-23",
        category="protection-sleeve",
        description="PS-23 Protection Sleeve"
    )
    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LO-thumb.png")
    PS_23.thumbnail_image = thumb
    illu_left, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/pro-sleeve-l.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    PS_23.illustration_images.add(illu_left)
    illu_middle, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-23-BodySpan-h50.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    PS_23.illustration_images.add(illu_middle)
    illu_right, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/pro-sleeve-r.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    PS_23.illustration_images.add(illu_right)
    demo, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/LO-thumb.png")
    PS_23.description_images.add(demo)
    PS_23.save()

    sleeves, created = AtomicGroup.objects.get_or_create(name="sleeves")
    sleeves.members.add(LO_23, PS_23)
    sleeves.save()


def run():

    createEndfitting()
    createExtender()
    createSleeves()


