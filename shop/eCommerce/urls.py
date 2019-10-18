from django.conf.urls import url

from shop.eCommerce.api import (
    # ECOMProduct
    ECOMProductList,
    ECOMProductDetails,
    ECOMProductCreate,
    ECOMProductUpdate,
    ECOMProductDestroy,
    # ECOMProductImage
    ECOMProductImageList,
    ECOMProductImageDetails,
    ECOMProductImageCreate,
    ECOMProductImageUpdate,
    ECOMProductImageDestroy,
)

namespace_prefix = "shop.eCommerce."

urlpatterns = [
    # ECOMProduct
    url(r'^product/$', ECOMProductList.as_view(),
        name=namespace_prefix + "ECOMProduct.list"),
    url(r'^product/view/(?P<pk>\d+)/$', ECOMProductDetails.as_view(),
        name=namespace_prefix + "ECOMProduct.detail"),
    url(r'^product/create/', ECOMProductCreate.as_view(),
        name=namespace_prefix + "ECOMProduct.create"),
    url(r'^product/update/(?P<pk>\d+)/$', ECOMProductUpdate.as_view(),
        name=namespace_prefix + "ECOMProduct.update"),
    url(r'^product/delete/(?P<pk>\d+)/$', ECOMProductDestroy.as_view(),
        name=namespace_prefix + "ECOMProduct.destroy"),
    # # ECOMProductImage
    # url(r'^ECOMProductImage/$', ECOMProductImageList.as_view(),
    #     name=namespace_prefix + "ECOMProductImage.list"),
    # url(r'^ECOMProductImage/view/(?P<pk>\d+)/$', ECOMProductImageDetails.as_view(),
    #     name=namespace_prefix + "ECOMProductImage.detail"),
    # url(r'^ECOMProductImage/create/', ECOMProductImageCreate.as_view(),
    #     name=namespace_prefix + "ECOMProductImage.create"),
    # url(r'^ECOMProductImage/update/(?P<pk>\d+)/$', ECOMProductImageUpdate.as_view(),
    #     name=namespace_prefix + "ECOMProductImage.update"),
    # url(r'^ECOMProductImage/delete/(?P<pk>\d+)/$', ECOMProductImageDestroy.as_view(),
    #     name=namespace_prefix + "ECOMProductImage.destroy"),
]
