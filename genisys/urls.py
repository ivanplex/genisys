from django.contrib import admin
from django.conf.urls import include, url
from genisys.views import home
from rest_framework_swagger.views import get_swagger_view


def generate_url_include(name):
    regex = r'^{}/'.format(name)
    to_include = include('shop.{}.urls'.format(name))
    namespace = 'shop.{}'.format(name)
    return url(regex, to_include, name=namespace)

namespaces_to_include = [
    "atomic",
    "assembly",
    "attribute",
    "group",
]

namespaced_urls = [
    generate_url_include(name) for name in namespaces_to_include
]

schema_view = get_swagger_view(title='Genisys API')

urlpatterns = [
    url(r'^api/v1/', include([
        url(r'^docs/', schema_view),
        url(r'', include(namespaced_urls))
    ],
    ))
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
]
