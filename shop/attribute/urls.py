from django.conf.urls import url

from shop.attribute.api import (
    # Attribute
    AtomicAttributeList,
    AtomicAttributeDetails,
    AtomicAttributeCreate,
    AtomicAttributeUpdate,
    AtomicAttributeDestroy,
    # Blueprint Attribute
    BlueprintAttributeList,
    BlueprintAttributeDetails,
    BlueprintAttributeCreate,
    BlueprintAttributeUpdate,
    BlueprintAttributeDestroy,
    # Product Attribute
    ProductAttributeList,
    ProductAttributeDetails,
    ProductAttributeCreate,
    ProductAttributeUpdate,
    ProductAttributeDestroy,
)

namespace_prefix = "shop.attribute."

urlpatterns = [
    # Atomic Attribute
    url(r'^atomic/$', AtomicAttributeList.as_view(),
        name=namespace_prefix + "attribute.list"),
    url(r'^atomic/view/(?P<pk>\d+)/$', AtomicAttributeDetails.as_view(),
        name=namespace_prefix + "attribute.detail"),
    url(r'^atomic/create/$', AtomicAttributeCreate.as_view(),
        name=namespace_prefix + "attribute.create"),
    url(r'^atomic/update/(?P<pk>\d+)/$', AtomicAttributeUpdate.as_view(),
        name=namespace_prefix + "attribute.update"),
    url(r'^atomic/delete/(?P<pk>\d+)/$', AtomicAttributeDestroy.as_view(),
        name=namespace_prefix + "attribute.destroy"),
    # Blueprint Attribute
    url(r'^blueprint/$', BlueprintAttributeList.as_view(),
        name=namespace_prefix + "blueprint.list"),
    url(r'^blueprint/view/(?P<pk>\d+)/$', BlueprintAttributeDetails.as_view(),
        name=namespace_prefix + "component.detail"),
    url(r'^blueprint/create/', BlueprintAttributeCreate.as_view(),
        name=namespace_prefix + "component.create"),
    url(r'^blueprint/update/(?P<pk>\d+)/$', BlueprintAttributeUpdate.as_view(),
        name=namespace_prefix + "component.update"),
    url(r'^blueprint/delete/(?P<pk>\d+)/$', BlueprintAttributeDestroy.as_view(),
        name=namespace_prefix + "component.destroy"),
    # Product Attribute
    url(r'^product/$', ProductAttributeList.as_view(),
        name=namespace_prefix + "product.list"),
    url(r'^product/view/(?P<pk>\d+)/$', ProductAttributeDetails.as_view(),
        name=namespace_prefix + "product.detail"),
    url(r'^product/create/', ProductAttributeCreate.as_view(),
        name=namespace_prefix + "product.create"),
    url(r'^product/update/(?P<pk>\d+)/$', ProductAttributeUpdate.as_view(),
        name=namespace_prefix + "product.update"),
    url(r'^product/delete/(?P<pk>\d+)/$', ProductAttributeDestroy.as_view(),
        name=namespace_prefix + "product.destroy"),
]
