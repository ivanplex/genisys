from django.conf.urls import url

from shop.group.api import (
    # AtomicGroup
    AtomicGroupList,
    AtomicGroupDetails,
    AtomicGroupCreate,
    AtomicGroupUpdate,
    AtomicGroupDestroy,
    # BlueprintGroup
    BlueprintGroupList,
    BlueprintGroupDetails,
    BlueprintGroupCreate,
    BlueprintGroupUpdate,
    BlueprintGroupDestroy,
    # ProductGroup
    ProductGroupList,
    ProductGroupDetails,
    ProductGroupCreate,
    ProductGroupUpdate,
    ProductGroupDestroy,
)

namespace_prefix = "shop.group."

urlpatterns = [
    # Atomic Group
    url(r'^atomic/$', AtomicGroupList.as_view(),
        name=namespace_prefix + "atomic.list"),
    url(r'^atomic/view/(?P<pk>\d+)/$', AtomicGroupDetails.as_view(),
        name=namespace_prefix + "atomic.detail"),
    url(r'^atomic/create/$', AtomicGroupCreate.as_view(),
        name=namespace_prefix + "atomic.create"),
    url(r'^atomic/update/(?P<pk>\d+)/$', AtomicGroupUpdate.as_view(),
        name=namespace_prefix + "atomic.update"),
    url(r'^atomic/delete/(?P<pk>\d+)/$', AtomicGroupDestroy.as_view(),
        name=namespace_prefix + "atomic.destroy"),
    # Blueprint Group
    url(r'^blueprint/$', BlueprintGroupList.as_view(),
        name=namespace_prefix + "blueprint.list"),
    url(r'^blueprint/view/(?P<pk>\d+)/$', BlueprintGroupDetails.as_view(),
        name=namespace_prefix + "blueprint.detail"),
    url(r'^blueprint/create/$', BlueprintGroupCreate.as_view(),
        name=namespace_prefix + "blueprint.create"),
    url(r'^blueprint/update/(?P<pk>\d+)/$', BlueprintGroupUpdate.as_view(),
        name=namespace_prefix + "blueprint.update"),
    url(r'^blueprint/delete/(?P<pk>\d+)/$', BlueprintGroupDestroy.as_view(),
        name=namespace_prefix + "blueprint.destroy"),
    # Product Group
    url(r'^product/$', ProductGroupList.as_view(),
        name=namespace_prefix + "product.list"),
    url(r'^product/view/(?P<pk>\d+)/$', ProductGroupDetails.as_view(),
        name=namespace_prefix + "product.detail"),
    url(r'^product/create/$', ProductGroupCreate.as_view(),
        name=namespace_prefix + "product.create"),
    url(r'^product/update/(?P<pk>\d+)/$', ProductGroupUpdate.as_view(),
        name=namespace_prefix + "product.update"),
    url(r'^product/delete/(?P<pk>\d+)/$', ProductGroupDestroy.as_view(),
        name=namespace_prefix + "product.destroy"),
]
