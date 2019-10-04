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
    Product
)

from shop.assembly.serializers import (
    BlueprintSerializer,
    ProductSerializer
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

###
# Product
###


class ProductList(ListAPIView):
    """
        Returns list of Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(RetrieveAPIView):
    """
        Returns detail of a Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(CreateAPIView):
    """
        Create Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroy(DestroyAPIView):
    """
        Destroy Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
