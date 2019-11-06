from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.assembly.models import Blueprint
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintSerializer

from shop.configurator.serializers import GasSpringBlueprintSerializer


def show_models():
    material_list = Attribute.objects \
        .filter(blueprint_attr__members__name="Gas Spring") \
        .values_list('value', flat=True).distinct()

    tree = {}
    for material in material_list:
        gas_spring_models = Blueprint.objects.filter(attribute__value=material).values_list('name', flat=True)
        tree[material] = list(gas_spring_models)

    return Response(tree)

def get_models(gas_spring_model, required=True):
    return Blueprint.objects.filter(name=gas_spring_model).first()


@api_view(['GET', 'POST'])
def get_material_model(request):

    # ordered list
    steps = {'model':           1,
             'stroke':          1,
             'ext':             0,
             'rod_fitting':     1,
             'body_fitting':    1,
             'extended_length': 1,
             'force':           1
             }

    if request.method == 'GET':
        return show_models()

    if request.method == 'POST':
        gas_spring_model = request.data.get('model', None)
        if gas_spring_model is None:
            return show_models()
            # content = {'Error': "Incomplete dataset. Missing key `model`."}
            # return Response(content, status=status.HTTP_400_BAD_REQUEST)
        blueprint = Blueprint.objects.filter(name=gas_spring_model).first()
        if blueprint is None:
            content = {'Error': 'Gas spring model not found.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = GasSpringBlueprintSerializer(blueprint)
        return Response(serializer.data)
