from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)

from shop.group.models import AtomicGroup, ProductGroup
from shop.group.serializers import (
    AtomicGroupSerializer,
    ProductGroupSerializer
)


class AtomicGroupList(ListAPIView):
    """
        Returns list of AtomicGroup
    """
    queryset = AtomicGroup.objects.all()
    serializer_class = AtomicGroupSerializer


class AtomicGroupDetails(RetrieveAPIView):
    """
        Returns detail of an AtomicGroup
    """
    queryset = AtomicGroup.objects.all()
    serializer_class = AtomicGroupSerializer


class AtomicGroupCreate(CreateAPIView):
    """
        Create AtomicGroup
    """
    queryset = AtomicGroup.objects.all()
    serializer_class = AtomicGroupSerializer


class AtomicGroupUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update AtomicGroup
    """
    queryset = AtomicGroup.objects.all()
    serializer_class = AtomicGroupSerializer


class AtomicGroupDestroy(DestroyAPIView):
    """
        Destroy AtomicGroup
    """
    queryset = AtomicGroup.objects.all()
    serializer_class = AtomicGroupSerializer


######
# ProductGroup
######


class ProductGroupList(ListAPIView):
    """
        Returns list of ProductGroup
    """
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class ProductGroupDetails(RetrieveAPIView):
    """
        Returns detail of an ProductGroup
    """
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class ProductGroupCreate(CreateAPIView):
    """
        Create ProductGroup
    """
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class ProductGroupUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update ProductGroup
    """
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class ProductGroupDestroy(DestroyAPIView):
    """
        Destroy ProductGroup
    """
    queryset = ProductGroup.objects.all()
