import logging
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)
from shop.assembly.models import (
    Blueprint,
)

from shop.assembly.serializers import (
    BlueprintSerializer,
)

logger = logging.getLogger(__name__)


class BlueprintList(ListAPIView):
    """
        Returns list of AtomicComponent
    """
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer


class BlueprintDetails(RetrieveAPIView):
    """
        Returns detail of a Blueprint
    """
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer


class BlueprintCreate(CreateAPIView):
    """
        Create Blueprint
    """
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer


class BlueprintUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update Blueprint
    """
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer


class BlueprintDestroy(DestroyAPIView):
    """
        Destroy Blueprint
    """
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer

