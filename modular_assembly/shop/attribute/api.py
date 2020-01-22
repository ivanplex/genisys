# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     RetrieveUpdateDestroyAPIView,
#     CreateAPIView,
#     DestroyAPIView
# )
#
# from modular_assembly.atomic.models import AtomicAttribute
# from modular_assembly.atomic.serializers import AtomicAttributeSerializer
# from modular_assembly.assembly.models import BlueprintAttribute, ProductAttribute
# from modular_assembly.assembly.serializers import (
#     BlueprintAttributeSerializer,
#     ProductAttributeSerializer
# )
#
# #######
# # AtomicAttribute
# #######
#
#
# class AtomicAttributeList(ListAPIView):
#     """
#         Returns list of AtomicAttribute
#     """
#     queryset = AtomicAttribute.objects.all()
#     serializer_class = AtomicAttributeSerializer
#
#
# class AtomicAttributeDetails(RetrieveAPIView):
#     """
#         View AtomicAttribute
#     """
#     queryset = AtomicAttribute.objects.all()
#     serializer_class = AtomicAttributeSerializer
#
#
# class AtomicAttributeCreate(CreateAPIView):
#     """
#         Create AtomicAttribute
#     """
#     queryset = AtomicAttribute.objects.all()
#     serializer_class = AtomicAttributeSerializer
#
#
# class AtomicAttributeUpdate(RetrieveUpdateDestroyAPIView):
#     """
#         Update AtomicAttribute
#     """
#     queryset = AtomicAttribute.objects.all()
#     serializer_class = AtomicAttributeSerializer
#
#
# class AtomicAttributeDestroy(DestroyAPIView):
#     """
#         Destroy AtomicAttribute
#     """
#     queryset = AtomicAttribute.objects.all()
#     serializer_class = AtomicAttributeSerializer
#
# ###
# # Blueprint Attribute
# ###
#
#
# class BlueprintAttributeList(ListAPIView):
#     """
#         Returns list of BlueprintAttribute
#     """
#     queryset = BlueprintAttribute.objects.all()
#     serializer_class = BlueprintAttributeSerializer
#
#
# class BlueprintAttributeDetails(RetrieveAPIView):
#     """
#         Returns detail of a BlueprintAttribute
#     """
#     queryset = BlueprintAttribute.objects.all()
#     serializer_class = BlueprintAttributeSerializer
#
#
# class BlueprintAttributeCreate(CreateAPIView):
#     """
#         Create BlueprintAttribute
#     """
#     queryset = BlueprintAttribute.objects.all()
#     serializer_class = BlueprintAttributeSerializer
#
#
# class BlueprintAttributeUpdate(RetrieveUpdateDestroyAPIView):
#     """
#         Update BlueprintAttribute
#     """
#     queryset = BlueprintAttribute.objects.all()
#     serializer_class = BlueprintAttributeSerializer
#
#
# class BlueprintAttributeDestroy(DestroyAPIView):
#     """
#         Destroy BlueprintAttribute
#     """
#     queryset = BlueprintAttribute.objects.all()
#     serializer_class = BlueprintAttributeSerializer
#
# ###
# # Product Attribute
# ###
#
#
# class ProductAttributeList(ListAPIView):
#     """
#         Returns list of ProductAttribute
#     """
#     queryset = ProductAttribute.objects.all()
#     serializer_class = ProductAttributeSerializer
#
#
# class ProductAttributeDetails(RetrieveAPIView):
#     """
#         Returns detail of a ProductAttribute
#     """
#     queryset = ProductAttribute.objects.all()
#     serializer_class = ProductAttributeSerializer
#
#
# class ProductAttributeCreate(CreateAPIView):
#     """
#         Create ProductAttribute
#     """
#     queryset = ProductAttribute.objects.all()
#     serializer_class = ProductAttributeSerializer
#
#
# class ProductAttributeUpdate(RetrieveUpdateDestroyAPIView):
#     """
#         Update ProductAttribute
#     """
#     queryset = ProductAttribute.objects.all()
#     serializer_class = ProductAttributeSerializer
#
#
# class ProductAttributeDestroy(DestroyAPIView):
#     """
#         Destroy ProductAttribute
#     """
#     queryset = ProductAttribute.objects.all()
#     serializer_class = ProductAttributeSerializer
