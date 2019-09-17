from django.conf.urls import url

from shop.atomic.api import (
    AtomicComponentList,
    AtomicComponentCreate,
)

from shop.atomic.views import (
    view
)

namespace_prefix = "shop.atomic."

urlpatterns = [
    url(r'^component/$', AtomicComponentList.as_view(),
            name=namespace_prefix + "component.list"),
    url(r'^component/add/$', AtomicComponentCreate.as_view(),
            name=namespace_prefix + "component.list"),
    url(r'view/$', view,
                name=namespace_prefix + "view"),
]