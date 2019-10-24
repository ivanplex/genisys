from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.assembly.models import Blueprint
from shop.attribute.models import Attribute


@api_view(['GET'])
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
