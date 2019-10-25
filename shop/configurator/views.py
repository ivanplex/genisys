from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.assembly.models import Blueprint
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintSerializer

from shop.configurator.serializers import GasSpringBlueprintSerializer

@api_view(['GET', 'POST'])
def get_material_model(request):
    if request.method == 'GET':

        material_list = Attribute.objects\
            .filter(blueprint_attr__members__name="Gas Spring")\
            .values_list('value', flat=True).distinct()

        tree = {}
        for material in material_list:
            gas_spring_models = Blueprint.objects.filter(attribute__value=material).values_list('name', flat=True)
            tree[material] = list(gas_spring_models)

        return Response(tree)

    if request.method == 'POST':
        gas_spring_model = request.data.get('model', None)
        if gas_spring_model is None:
            content = {'Error': "Incomplete dataset. Missing key `model`."}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        blueprint = Blueprint.objects.filter(name=gas_spring_model).first()
        if blueprint is None:
            content = {'Error': 'Gas spring model not found.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = GasSpringBlueprintSerializer(blueprint)
        return Response(serializer.data)
