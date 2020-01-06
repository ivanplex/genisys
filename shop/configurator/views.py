from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.atomic.models import AtomicComponent, AtomicGroup
from shop.atomic.serializers import AtomicComponentConfiguratorSerializer
from shop.assembly.models import Blueprint, AtomicPrerequisite
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintConfiguratorSerializer
from shop.configurator.models import ConfiguratorStep
from shop.configurator.serializers import ConfiguratorStepSerializer
from shop.group.models import Group
from shop.group.serializers import GroupSerializer
from django.db.models import Q


def show_materials(required=True):
    material_group = Group.objects.filter(Q(name="Carbon") | Q(name="Stainless Steel"))
    serializer = GroupSerializer(material_group, many=True)
    return serializer.data


def show_models(group_id, required=True):

    group = Group.objects.get(pk=group_id)
    print(group.name)
    gas_spring_models = Blueprint.objects.filter(
        blueprint_attribute__key="material",
        blueprint_attribute__value=group.name
    )
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


def fetchUserResponse(requestData):
    # Fetch user specification response from POST request data
    data = {}
    steps = ConfiguratorStep.objects.filter(disabled=False).order_by('id')
    for step in steps:
        data[step.slug] = requestData.get(step.slug, None)
    return data

def fetchStepField(slug):
    # Fetch serialized field JSON
    field = ConfiguratorStep.objects.filter(disabled=False, slug=slug).first()
    serialData = ConfiguratorStepSerializer(field).data
    return serialData


@api_view(['POST'])
def interactions(request):
    steps = ConfiguratorStep.objects.filter(disabled=False).order_by('id')

    # As of Python 3.6, dictionary guarantee insertion order
    json = {}
    for step in steps:
        json[step.slug] = fetchStepField(step.slug)

    response = fetchUserResponse(request.data)

    methods = {
        'material': show_materials,
        'model': show_models,
        'stroke': show_stroke_length,
        'extension': show_extension,
        'sleeves': show_sleeves,
        'rod-fitting': show_rod_fitting,
        'body-fitting': show_body_fitting,
        'extended_length': show_extended_length,
        'force': show_force
    }


    # pre-populate material if material not selected
    if response['material'] is None:
        json['material']['selected'] = show_materials()[0].get("id")
        json['model']['options'] = show_models(show_materials()[0].get("id"))

    # raw_steps[0]['options'] = show_materials()
    # if response.material is not None:
    #     raw_steps[0]['selected'] = response.material
    #     raw_steps[1]['options'] = show_models(response.material)
    #     if response.model is not None:
    #         raw_steps[1]['selected'] = response.model
    #         raw_steps[2]['range'] = show_stroke_length(response.model)
    #         if response.stroke is not None:
    #             raw_steps[2]['selected'] = response.stroke
    #             raw_steps[3]['options'] = show_extension(response.model)
    #             if response.extension is not None:
    #                 raw_steps[3]['selected'] = response.extension
    #                 raw_steps[4]['options'] = show_sleeves(response.model)
    #
    #                 if response.sleeves is not None:
    #                     raw_steps[4]['selected'] = response.sleeves
    #                     raw_steps[5]['options'] = show_rod_fitting(response.model)
    #
    #                     if response.rod_fitting is not None:
    #                         raw_steps[5]['selected'] = response.rod_fitting
    #                         raw_steps[6]['options'] = show_body_fitting(response.model)
    #                         if response.body_fitting is not None:
    #                             raw_steps[6]['selected'] = response.body_fitting
    #                             raw_steps[7]['range'] = show_extended_length(response.model)
    #                             if response.extended_length is not None:
    #                                 raw_steps[7]['selected'] = response.extended_length
    #                                 raw_steps[8]['range'] = show_force(response.model)
    #                                 raw_steps[8]['selected'] = raw_steps[8]['range']['minimum']  # Set default as minimum
    #                                 if response.force is not None:
    #                                     raw_steps[8]['selected'] = response.force

    

    return Response(json)

