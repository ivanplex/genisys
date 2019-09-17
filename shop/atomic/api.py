import logging
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)
from shop.atomic.models import AtomicComponent, AtomicPrerequisite
from shop.atomic.serializers import (
    AtomicComponentSerializer,
    AtomicPrerequisiteSerializer,
)

logger = logging.getLogger(__name__)


class AtomicComponentList(ListAPIView):
    """
        Returns list of AtomicComponent
    """
    queryset = AtomicComponent.objects.all()
    serializer_class = AtomicComponentSerializer


class AtomicComponentDetails(RetrieveAPIView):
    queryset = AtomicComponent.objects.all()
    serializer_class = AtomicComponentSerializer


class AtomicComponentCreate(CreateAPIView):
    """
        Create AtomicComponent
    """
    queryset = AtomicComponent.objects.all()
    serializer_class = AtomicComponentSerializer


class AtomicComponentUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update AtomicComponent
    """
    queryset = AtomicComponent.objects.all()
    serializer_class = AtomicComponentSerializer


class AtomicComponentDestroy(DestroyAPIView):
    """
        Destroy AtomicComponent
    """
    queryset = AtomicComponent.objects.all()
    serializer_class = AtomicComponentSerializer


class AtomicPrerequisiteDetails(RetrieveAPIView):
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer

