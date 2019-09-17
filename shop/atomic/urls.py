from django.conf.urls import url

from shop.atomic.api import (
    AtomicComponentList
)

namespace_prefix = "shop.atomic."

urlpatterns = [
        url(r'^$', AtomicComponentList.as_view(),
                name=namespace_prefix + "list"),
]