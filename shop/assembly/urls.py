from django.conf.urls import url

from shop.assembly.api import (
    # Blueprint
    BlueprintList,
    BlueprintDetails,
    BlueprintCreate,
    BlueprintUpdate,
    BlueprintDestroy,
)

namespace_prefix = "shop.assembly."

urlpatterns = [
    # Component
    url(r'^blueprint/$', BlueprintList.as_view(),
            name=namespace_prefix + "blueprint.list"),
    url(r'^blueprint/view/(?P<pk>\d+)/$', BlueprintDetails.as_view(),
            name=namespace_prefix + "component.detail"),
    url(r'^blueprint/create/', BlueprintCreate.as_view(),
            name=namespace_prefix + "component.create"),
    url(r'^blueprint/update/(?P<pk>\d+)/$', BlueprintUpdate.as_view(),
        name=namespace_prefix + "component.update"),
    url(r'^blueprint/delete/(?P<pk>\d+)/$', BlueprintDestroy.as_view(),
        name=namespace_prefix + "component.destroy"),
]