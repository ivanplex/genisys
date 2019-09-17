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
