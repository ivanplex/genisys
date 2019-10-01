from django.conf.urls import url

from shop.group.api import (
    # AtomicGroup
    AtomicGroupList,
    AtomicGroupDetails,
    AtomicGroupCreate,
    AtomicGroupUpdate,
    AtomicGroupDestroy,
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
]
