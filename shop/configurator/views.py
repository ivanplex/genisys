from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.assembly.models import Blueprint, AtomicPrerequisite
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintConfiguratorSerializer
from shop.configurator.models import ConfiguratorStep
from shop.configurator.serializers import ConfiguratorStepSerializer


def show_materials(required=True):
    material_list = Attribute.objects \
        .filter(blueprint_attr__members__name="Gas Spring") \
        .values_list('value', flat=True).distinct()

    material_id_mapping = {
        'Super Duplex': 1,
        'Carbon': 2,
        'Titanium': 3,
        'Stainless Steel': 4,
    }
    l = []
    for material in material_list:
        if material in material_id_mapping.keys():
            l.append({
                    'id': material_id_mapping.get(material),
                    'material': material,
                    'thumb_image': 'https://dummyimage.com/50',
                    'illustration_image': 'https://dummyimage.com/300'
                }
            )
    return l


def show_models(material_id, required=True):
    material_id_mapping = {
        1: 'Super Duplex',
        2: 'Carbon',
        3: 'Titanium',
        4: 'Stainless Steel'
    }

    gas_spring_models = Blueprint.objects.filter(attribute__value=material_id_mapping.get(material_id))
    serializer = BlueprintConfiguratorSerializer(gas_spring_models, many=True)
    return serializer.data


def show_stroke_length(model_id, required=True):
    # blueprint = Blueprint.objects.filter(id=model_id).first()
    return [{
        'minimum': 5,
        'maximum': 70
    }]

@api_view(['GET', 'POST'])
def interactions(request):
    if request.method == 'POST':
        steps = ConfiguratorStep.objects.all()
        raw_steps = ConfiguratorStepSerializer(steps, many=True).data

        material = request.data.get('material', None)
        model = request.data.get('model', None)

        if model is not None:
            raw_steps[0]['selected'] = material
            raw_steps[1]['selected'] = model
            raw_steps[2]['options'] = show_stroke_length(material)
        elif material is not None:
            raw_steps[0]['selected'] = material
            raw_steps[1]['options'] = show_models(material)
        else:
            raw_steps[0]['options'] = show_materials()

        return Response(raw_steps)



    # # ordered list
    # steps = {
    #          'material':        1,
    #          'model':           1,
    #          'stroke':          1,
    #          'ext':             0,
    #          'rod_fitting':     1,
    #          'body_fitting':    1,
    #          'extended_length': 1,
    #          'force':           1
    #          }
    #
    # if request.method == 'GET':
    #     return show_materials()
    #
    # if request.method == 'POST':
    #     material = request.data.get('material', None)
    #     if material is None:
    #         return show_materials()
    #     else:
    #         return show_models(material)


        # gas_spring_model = request.data.get('model', None)
        # if gas_spring_model is None:
        #     return show_models(gas_spring_model)

            # content = {'Error': "Incomplete dataset. Missing key `model`."}
            # return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # blueprint = Blueprint.objects.filter(name=gas_spring_model).first()
        # if blueprint is None:
        #     content = {'Error': 'Gas spring model not found.'}
        #     return Response(content, status=status.HTTP_404_NOT_FOUND)
        # serializer = GasSpringBlueprintSerializer(blueprint)
        # return Response(serializer.data)
