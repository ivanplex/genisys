from django.conf.urls import url
from shop.configurator import views

urlpatterns = [
    url(r'', views.get_material_model),
]