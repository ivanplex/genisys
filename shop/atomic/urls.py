from django.conf.urls import url

from shop.atomic.api import (
    AtomicComponentList,
    AtomicComponentDetails,
    AtomicComponentCreate,
    AtomicComponentUpdate,
    AtomicComponentDestroy,
)

from shop.atomic.views import (
    view
)

namespace_prefix = "shop.atomic."

urlpatterns = [
    url(r'^component/$', AtomicComponentList.as_view(),
            name=namespace_prefix + "component.list"),
    url(r'^component/view/(?P<pk>\d+)/$', AtomicComponentDetails.as_view(),
            name=namespace_prefix + "component.detail"),
    url(r'^component/create/$', AtomicComponentCreate.as_view(),
            name=namespace_prefix + "component.create"),
    url(r'^component/update/(?P<pk>\d+)/$', AtomicComponentUpdate.as_view(),
            name=namespace_prefix + "component.update"),
    url(r'^component/delete/(?P<pk>\d+)/$', AtomicComponentDestroy.as_view(),
            name=namespace_prefix + "component.destory"),
    url(r'view/$', view,
                name=namespace_prefix + "view"),
]