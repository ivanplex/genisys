from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fail/$', views.fail),
    url(r'^createComponents/$', views.createComponents),
    url(r'^createTableBlueprint/$', views.createTableBlueprint),
]