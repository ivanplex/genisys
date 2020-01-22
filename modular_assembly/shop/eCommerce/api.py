from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)

from modular_assembly.eCommerce.models import (
    ECOMProduct,
    ECOMProductImage,
)

from modular_assembly.eCommerce.serializers import (
    ECOMProductSerializer,
    ECOMProductImageSerializer,
)


class ECOMProductList(ListAPIView):
    """
        Returns list of ECOMProduct
    """
    queryset = ECOMProduct.objects.all()
    serializer_class = ECOMProductSerializer


class ECOMProductDetails(RetrieveAPIView):
    """
        Returns detail of an ECOMProduct
    """
    queryset = ECOMProduct.objects.all()
    serializer_class = ECOMProductSerializer


class ECOMProductCreate(CreateAPIView):
    """
        Create ECOMProduct
    """
    queryset = ECOMProduct.objects.all()
    serializer_class = ECOMProductSerializer


class ECOMProductUpdate(RetrieveUpdateDestroyAPIView):
    """
        Update ECOMProduct
    """
    queryset = ECOMProduct.objects.all()
    serializer_class = ECOMProductSerializer


class ECOMProductDestroy(DestroyAPIView):
    """
        Destroy ECOMProduct
    """
    queryset = ECOMProduct.objects.all()
    serializer_class = ECOMProductSerializer


######
# ECOMProductImage
######


# class ECOMProductImageList(ListAPIView):
#     """
#         Returns list of ECOMProductImage
#     """
#     queryset = ECOMProductImage.objects.all()
#     serializer_class = ECOMProductImageSerializer
#
#
# class ECOMProductImageDetails(RetrieveAPIView):
#     """
#         Returns detail of an ECOMProductImage
#     """
#     queryset = ECOMProductImage.objects.all()
#     serializer_class = ECOMProductImageSerializer
#
#
# class ECOMProductImageCreate(CreateAPIView):
#     """
#         Create ECOMProductImage
#     """
#     queryset = ECOMProductImage.objects.all()
#     serializer_class = ECOMProductImageSerializer
#
#
# class ECOMProductImageUpdate(RetrieveUpdateDestroyAPIView):
#     """
#         Update ECOMProductImage
#     """
#     queryset = ECOMProductImage.objects.all()
#     serializer_class = ECOMProductImageSerializer
#
#
# class ECOMProductImageDestroy(DestroyAPIView):
#     """
#         Destroy ECOMProductImage
#     """
#     queryset = ECOMProductImage.objects.all()
#     serializer_class = ECOMProductImageSerializer
