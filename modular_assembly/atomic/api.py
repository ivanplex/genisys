import logging


from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)
from modular_assembly.atomic.models import (
    AtomicComponent,
    AtomicPrerequisite,
    AtomicSpecification
)

from modular_assembly.atomic.serializers import (
    AtomicComponentSerializer,
    AtomicPrerequisiteSerializer,
    AtomicSpecificationSerializer
)

logger = logging.getLogger(__name__)


class AtomicComponentList(ListAPIView):
    """
        Returns list of AtomicComponent
    """
    queryset = AtomicComponent.objects.all()
    serializer_class = AtomicComponentSerializer


class AtomicComponentDetails(RetrieveAPIView):
    """
        Returns detail of an AtomicComponent
    """
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


class AtomicPrerequisiteList(ListAPIView):
    """
        Returns list of AtomicPrerequisite
    """
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer


class AtomicPrerequisiteDetails(RetrieveAPIView):
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer


class AtomicPrerequisiteCreate(CreateAPIView):
    """
        Create AtomicPrerequisite
    """
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer


class AtomicPrerequisiteUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update AtomicPrerequisite
    """
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer


class AtomicPrerequisiteDestroy(DestroyAPIView):
    """
        Destroy AtomicPrerequisite
    """
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer


class AtomicSpecificationList(ListAPIView):
    """
        Returns list of AtomicSpecification
    """
    queryset = AtomicSpecification.objects.all()
    serializer_class = AtomicSpecificationSerializer


class AtomicSpecificationDetails(RetrieveAPIView):
    """
        View AtomicSpecification
    """
    queryset = AtomicSpecification.objects.all()
    serializer_class = AtomicSpecificationSerializer


class AtomicSpecificationCreate(CreateAPIView):
    """
        Create AtomicSpecification
    """
    queryset = AtomicPrerequisite.objects.all()
    serializer_class = AtomicPrerequisiteSerializer


class AtomicSpecificationUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update AtomicSpecification
    """
    queryset = AtomicSpecification.objects.all()
    serializer_class = AtomicSpecificationSerializer


class AtomicSpecificationDestroy(DestroyAPIView):
    """
        Destroy AtomicSpecification
    """
    queryset = AtomicSpecification.objects.all()
    serializer_class = AtomicSpecificationSerializer
