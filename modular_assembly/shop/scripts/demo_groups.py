from modular_assembly.group.models import Group, URL, OffsetImageURL

def createCarbonGroup():
    carbon, created = Group.objects.get_or_create(name="Carbon", description="Carbon Gas springs")

    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/E+-+Carbon+Steel+Painted-Current+View.png")
    carbon.thumbnail_image = thumb
    illu_left, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodyEnd-h50-l.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    carbon.illustration_images.add(illu_left)
    illu_middle, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodySpan-h50.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    carbon.illustration_images.add(illu_middle)
    illu_right, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodyEnd-h50-r.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    carbon.illustration_images.add(illu_right)
    carbon.save()

def createStainlessSteelGroup():
    SS, created = Group.objects.get_or_create(name="Stainless Steel", description="Stainless Steel Gas springs")

    thumb, created = URL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/S+-+Stainless+Steel-Current+View.png")
    SS.thumbnail_image = thumb
    illu_left, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodyEnd-h50-l.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    SS.illustration_images.add(illu_left)
    illu_middle, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodySpan-h50.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    SS.illustration_images.add(illu_middle)
    illu_right, created = OffsetImageURL.objects.get_or_create(
        url="https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodyEnd-h50-r.png",
        offset_x=0,
        offset_y=0,
        position=0
    )
    SS.illustration_images.add(illu_right)
    SS.save()

def run():
    # Create material groups
    createCarbonGroup()
    createStainlessSteelGroup()
