from django.conf.urls import url

from shop.atomic.api import (
    # Component
    AtomicComponentList,
    AtomicComponentDetails,
    AtomicComponentCreate,
    AtomicComponentUpdate,
    AtomicComponentDestroy,
    # Prerequisite
    AtomicPrerequisiteList,
    AtomicPrerequisiteDetails,
    AtomicPrerequisiteCreate,
    AtomicPrerequisiteUpdate,
    AtomicPrerequisiteDestroy,

    # Specification
    AtomicSpecificationList,
    AtomicSpecificationDetails,
    AtomicSpecificationCreate,
    AtomicSpecificationUpdate,
    AtomicSpecificationDestroy,
)

from shop.atomic.views import (
    view
)

namespace_prefix = "shop.atomic."

urlpatterns = [
    # Component
    url(r'^component/$', AtomicComponentList.as_view(),
        name=namespace_prefix + "component.list"),
    url(r'^component/view/(?P<pk>\d+)/$', AtomicComponentDetails.as_view(),
        name=namespace_prefix + "component.detail"),
    url(r'^component/create/$', AtomicComponentCreate.as_view(),
        name=namespace_prefix + "component.create"),
    url(r'^component/update/(?P<pk>\d+)/$', AtomicComponentUpdate.as_view(),
        name=namespace_prefix + "component.update"),
    url(r'^component/delete/(?P<pk>\d+)/$', AtomicComponentDestroy.as_view(),
        name=namespace_prefix + "component.destroy"),
    # Prerequisite
    url(r'^prerequisite/$', AtomicPrerequisiteList.as_view(),
        name=namespace_prefix + "prerequisite.list"),
    url(r'^prerequisite/view/(?P<pk>\d+)/$', AtomicPrerequisiteDetails.as_view(),
        name=namespace_prefix + "prerequisite.detail"),
    url(r'^prerequisite/create/$', AtomicPrerequisiteCreate.as_view(),
        name=namespace_prefix + "prerequisite.create"),
    url(r'^prerequisite/update/(?P<pk>\d+)/$', AtomicPrerequisiteUpdate.as_view(),
        name=namespace_prefix + "prerequisite.update"),
    url(r'^prerequisite/delete/(?P<pk>\d+)/$', AtomicPrerequisiteDestroy.as_view(),
        name=namespace_prefix + "prerequisite.destroy"),
    # Specification
    url(r'^specification/$', AtomicSpecificationList.as_view(),
        name=namespace_prefix + "specification.list"),
    url(r'^specification/view/(?P<pk>\d+)/$', AtomicSpecificationDetails.as_view(),
        name=namespace_prefix + "specification.detail"),
    url(r'^specification/create/$', AtomicSpecificationCreate.as_view(),
        name=namespace_prefix + "specification.create"),
    url(r'^specification/update/(?P<pk>\d+)/$', AtomicSpecificationUpdate.as_view(),
        name=namespace_prefix + "specification.update"),
    url(r'^specification/delete/(?P<pk>\d+)/$', AtomicSpecificationDestroy.as_view(),
        name=namespace_prefix + "specification.destroy"),

    url(r'view/$', view,
        name=namespace_prefix + "view"),
]
