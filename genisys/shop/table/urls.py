from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^init/$', views.init),
    url(r'^available/$', views.available),
    url(r'^createComponents/$', views.createComponents),
    url(r'^createTableBlueprint/$', views.createTableBlueprint),
]