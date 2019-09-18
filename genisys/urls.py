from django.contrib import admin
from django.conf.urls import include, url


def generate_url_include(name):
    regex = r'^{}/'.format(name)
    to_include = include('shop.{}.urls'.format(name))
    namespace = 'shop.{}'.format(name)
    return url(regex, to_include, name=namespace)

namespaces_to_include = [
    "atomic",
    "assembly",
]

namespaced_urls = [
    generate_url_include(name) for name in namespaces_to_include
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^shop/', include('shop.urls')),
    url(r'', include(namespaced_urls)),
]
