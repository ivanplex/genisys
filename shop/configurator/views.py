from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.assembly.models import Blueprint, AtomicPrerequisite
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintSerializer

from shop.configurator.serializers import GasSpringBlueprintSerializer


def show_materials(required=True):
    material_list = Attribute.objects \
        .filter(blueprint_attr__members__name="Gas Spring") \
        .values_list('value', flat=True).distinct()

    return Response(
        {
            'configuration_step_title': 'Material',
            'configuration_step_description': '',
            'configuration_entry_type': 'selection_box',
            'configuration_step_slug': 'material',
            'configuration_next_step_slug': 'models',
            'options': list(material_list)
        }
    )


def show_models(gas_spring_material, required=True):

    gas_spring_models = Blueprint.objects.filter(attribute__value=gas_spring_material)
    serializer = BlueprintSerializer(gas_spring_models, many=True)
    # return Response(serializer.data)
    return Response(
            {
                'configuration_step_title': 'Models',
                'configuration_step_description': '',
                'configuration_entry_type': 'selection_box',
                'configuration_step_slug': 'model',
                'configuration_next_step_slug': 'stroke',
                'options': serializer.data
            }
        )

# def select_stroke_length(model_id, required=True):
#     stroke_length_attr = AtomicPrerequisite.objects.filter().first()
#     gas_spring.atomic_compo
#     #TODO:
#     min=10
#     max=20
#     return Response(
#         {
#             'configuration_step_title': 'Stroke Length',
#             'configuration_step_description': '',
#             'configuration_entry_type': 'numerical_range_selection',
#             'configuration_step_slug': 'stroke',
#             'configuration_next_step_slug': 'ext',
#             'options': [
#                 {
#                     'minimum': min,
#                     'maximum': max,
#                 }
#             ]
#         }
#     )


@api_view(['GET', 'POST'])
def get_material_model(request):

    # ordered list
    steps = {
             'material':        1,
             'model':           1,
             'stroke':          1,
             'ext':             0,
             'rod_fitting':     1,
             'body_fitting':    1,
             'extended_length': 1,
             'force':           1
             }

    if request.method == 'GET':
        return show_materials()

    if request.method == 'POST':
        material = request.data.get('material', None)
        if material is None:
            return show_materials()
        else:
            return show_models(material)


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
