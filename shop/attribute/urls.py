from django.conf.urls import url

from shop.assembly.api import (
    BlueprintAttributeList,
    BlueprintAttributeDetails,
    BlueprintAttributeCreate,
    BlueprintAttributeUpdate,
    BlueprintAttributeDestroy,
)

namespace_prefix = "shop.attribute."

urlpatterns = [
    # Blueprint
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
    # Product
    # url(r'^product/$', ProductList.as_view(),
    #     name=namespace_prefix + "product.list"),
    # url(r'^product/view/(?P<pk>\d+)/$', ProductDetails.as_view(),
    #     name=namespace_prefix + "product.detail"),
    # url(r'^product/create/', ProductCreate.as_view(),
    #     name=namespace_prefix + "product.create"),
    # url(r'^product/update/(?P<pk>\d+)/$', ProductUpdate.as_view(),
    #     name=namespace_prefix + "product.update"),
    # url(r'^product/delete/(?P<pk>\d+)/$', ProductDestroy.as_view(),
    #     name=namespace_prefix + "product.destroy"),
]
