from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)

from shop.group.models import AtomicGroup, BlueprintGroup, ProductGroup
from shop.group.serializers import (
    AtomicGroupSerializer,
    BlueprintGroupSerializer,
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
# BlueprintGroup
######


class BlueprintGroupList(ListAPIView):
    """
        Returns list of BlueprintGroup
    """
    queryset = BlueprintGroup.objects.all()
    serializer_class = BlueprintGroupSerializer


class BlueprintGroupDetails(RetrieveAPIView):
    """
        Returns detail of an BlueprintGroup
    """
    queryset = BlueprintGroup.objects.all()
    serializer_class = BlueprintGroupSerializer


class BlueprintGroupCreate(CreateAPIView):
    """
        Create BlueprintGroup
    """
    queryset = BlueprintGroup.objects.all()
    serializer_class = BlueprintGroupSerializer


class BlueprintGroupUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update BlueprintGroup
    """
    queryset = BlueprintGroup.objects.all()
    serializer_class = BlueprintGroupSerializer


class BlueprintGroupDestroy(DestroyAPIView):
    """
        Destroy BlueprintGroup
    """
    queryset = BlueprintGroup.objects.all()
    serializer_class = BlueprintGroupSerializer


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
    serializer_class = ProductGroupSerializer
