import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)
from shop.utils import Utils
from shop.atomic.models import AtomicComponent
from shop.atomic.serializers import (
    AtomicComponentSerializer,
)


class AtomicComponentList(ListAPIView):
    """
        Returns list of AtomicComponent
    """
    serializer_class = AtomicComponentSerializer

    def get_queryset(self):
        return AtomicComponent.objects.all()

class AtomicComponentCreate(CreateAPIView):
    """
        Create AtomicComponent
    """
    serializer_class = AtomicComponentSerializer

    def create(self,request,*args,**kwargs):
        try:
            atom = AtomicComponent.objects.create(
                stock_code=self.request.data.get('stock_code'),
                part_code=self.request.data.get('part_code'),
                description=self.request.data.get('description'),
                warehouse_location=self.request.data.get('warehouse_location'),
                material=self.request.data.get('material'),
                weight=self.request.data.get('weight'),
            )
            return Response(
                AtomicComponentSerializer(
                    AtomicComponent.objects.filter(id=atom.id).first(),
                    context={'request': self.request}).data,
                    status=status.HTTP_200_OK
                )
        except:
            return Utils.error_response_400('Please specify all parameters')

