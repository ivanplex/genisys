from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.atomic.models import AtomicComponent, AtomicGroup
from shop.atomic.serializers import AtomicComponentConfiguratorSerializer
from shop.assembly.models import Blueprint, AtomicPrerequisite
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintConfiguratorSerializer
from shop.configurator.models import ConfiguratorStep
from shop.configurator.serializers import ConfiguratorStepSerializer
from django.db.models import Q


def show_materials(required=True):
    return [
            {
                "id": 2,
                "name": "Carbon",
                "thumbnail_image": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/E+-+Carbon+Steel+Painted-Current+View.png",
                "illustration_images": [
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodyEnd-h50-l.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodySpan-h50.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodyEnd-h50-r.png",
                        "offset_x": 0,
                        "offset_y": 0
                    }
                ],
                "description_images": []
            },
            {
                "id": 4,
                "name": "Stainless Steel",
                "thumbnail_image": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/S+-+Stainless+Steel-Current+View.png",
                "illustration_images": [
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodyEnd-h50-l.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodySpan-h50.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodyEnd-h50-r.png",
                        "offset_x": 0,
                        "offset_y": 0
                    }
                ],
                "description_images": []
            }
        ]


def show_models(material_id, required=True):
    material_id_mapping = {
        1: 'Super Duplex',
        2: 'Carbon',
        3: 'Titanium',
        4: 'Stainless Steel'
    }

    # attr = Attribute.objects.filter(value=material_id_mapping.get(material_id)).first()
    # gas_spring_models = Blueprint.objects.filter(
    #     Q(attribute=attr)
    # )
    gas_spring_models = Blueprint.objects.filter(
        blueprint_attribute__key="material",
        blueprint_attribute__value=material_id_mapping.get(material_id))
    serializer = BlueprintConfiguratorSerializer(gas_spring_models, many=True)
    return serializer.data


def show_stroke_length(model_id, required=True):
    blueprint = Blueprint.objects.filter(id=model_id).first()
    stroke = blueprint.atomic_prerequisites.filter(name="stroke").first()
    return {
        'minimum': stroke.min_quantity,
        'maximum': stroke.max_quantity
    }

def show_extension(model_id):
    blueprint = Blueprint.objects.get(id=model_id)
    prereq = blueprint.atomic_prerequisites.filter(name="extender").first()
    extensions = AtomicComponent.objects.filter(requires=prereq)
    serializer = AtomicComponentConfiguratorSerializer(extensions, many=True)
    empty = [{
                "id": "null",
                "name": "None",
                "thumbnail_image": "https://dummyimage.com/100",
                "illustration_images": [],
                "description_images": [],
                "retail_price": 0.0,
                "retail_price_per_unit": 0.0,
                "retail_unit_measurement": "null",
                "component_factor": 0
            }]
    return empty + serializer.data


def show_sleeves(model_id):
    blueprint = Blueprint.objects.get(id=model_id)
    prereq = blueprint.atomic_prerequisites.filter(name="sleeve").first()
    group = prereq.atomic_group
    sleeves = AtomicComponent.objects.filter(members=group)
    serializer = AtomicComponentConfiguratorSerializer(sleeves, many=True)
    empty = [{
                "id": "null",
                "name": "None",
                "thumbnail_image": "https://dummyimage.com/100",
                "illustration_images": [],
                "description_images": [],
                "retail_price": 0.0,
                "retail_price_per_unit": 0.0,
                "retail_unit_measurement": "null",
                "component_factor": 0
            }]
    return empty + serializer.data


def show_rod_fitting(model_id):
    blueprint = Blueprint.objects.get(id=model_id)
    prereq = blueprint.atomic_prerequisites.filter(name="rod fitting").first()
    group = prereq.atomic_group
    fittings = AtomicComponent.objects.filter(members=group)
    serializer = AtomicComponentConfiguratorSerializer(fittings, many=True)
    empty = [{
        "id": "null",
        "name": "None",
        "thumbnail_image": "https://dummyimage.com/100",
        "illustration_images": [],
        "description_images": [],
        "retail_price": 0.0,
        "retail_price_per_unit": 0.0,
        "retail_unit_measurement": "null",
        "component_factor": 0
    }]
    return empty + serializer.data


def show_body_fitting(model_id):
    blueprint = Blueprint.objects.get(id=model_id)
    prereq = blueprint.atomic_prerequisites.filter(name="body fitting").first()
    group = prereq.atomic_group
    fittings = AtomicComponent.objects.filter(members=group)
    serializer = AtomicComponentConfiguratorSerializer(fittings, many=True)
    empty = [{
        "id": "null",
        "name": "None",
        "thumbnail_image": "https://dummyimage.com/100",
        "illustration_images": [],
        "description_images": [],
        "retail_price": 0.0,
        "retail_price_per_unit": 0.0,
        "retail_unit_measurement": "null",
        "component_factor": 0
    }]
    return empty + serializer.data


def show_extended_length(model_id):
    blueprint = Blueprint.objects.filter(id=model_id).first()
    length = blueprint.atomic_prerequisites.filter(name="extended length").first()
    return {
        'minimum': length.min_quantity,
        'maximum': length.max_quantity
    }

def show_force(model_id):
    blueprint = Blueprint.objects.filter(id=model_id).first()
    force = blueprint.atomic_prerequisites.filter(name="force").first()
    return {
        'minimum': force.min_quantity,
        'maximum': force.max_quantity
    }


@api_view(['POST'])
def interactions(request):
    if request.method == 'POST':
        steps = ConfiguratorStep.objects.filter(disabled=False).order_by('id')
        raw_steps = ConfiguratorStepSerializer(steps, many=True).data

        material = request.data.get('material', None)
        model = request.data.get('model', None)
        stroke = request.data.get('stroke', None)
        extension = request.data.get('extension', None)
        sleeves = request.data.get('sleeves', None)
        rod_fitting = request.data.get('rod-fitting', None)
        body_fitting = request.data.get('body-fitting', None)
        extended_length = request.data.get('extended_length', None)
        force = request.data.get('force', None)

        # pre-populate material if material not selected
        if material is None:
            raw_steps[0]['selected'] = show_materials()[0].get("id")
            raw_steps[1]['options'] = show_models(show_materials()[0].get("id"))

        raw_steps[0]['options'] = show_materials()
        if material is not None:
            raw_steps[0]['selected'] = material
            raw_steps[1]['options'] = show_models(material)
            if model is not None:
                raw_steps[1]['selected'] = model
                raw_steps[2]['range'] = show_stroke_length(model)
                if stroke is not None:
                    raw_steps[2]['selected'] = stroke
                    raw_steps[3]['options'] = show_extension(model)
                    if extension is not None:
                        raw_steps[3]['selected'] = extension
                        raw_steps[4]['options'] = show_sleeves(model)

                        if sleeves is not None:
                            raw_steps[4]['selected'] = sleeves
                            raw_steps[5]['options'] = show_rod_fitting(model)

                            if rod_fitting is not None:
                                raw_steps[5]['selected'] = rod_fitting
                                raw_steps[6]['options'] = show_body_fitting(model)
                                if body_fitting is not None:
                                    raw_steps[6]['selected'] = body_fitting
                                    raw_steps[7]['range'] = show_extended_length(model)
                                    if extended_length is not None:
                                        raw_steps[7]['selected'] = extended_length
                                        raw_steps[8]['range'] = show_force(model)
                                        if force is not None:
                                            raw_steps[8]['selected'] = force

        return Response(raw_steps)

