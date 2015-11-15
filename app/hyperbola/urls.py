from django.conf.urls import include, url
import django.contrib.admin
import django.contrib.admindocs.urls

from hyperbola import settings
import hyperbola.contact.urls
import hyperbola.frontpage.urls
import hyperbola.lifestream.urls
from hyperbola.helpers.views import NotFound404View


urlpatterns = [
    url(r'^$', include(hyperbola.frontpage.urls)),
    url(r'^contact/', include(hyperbola.contact.urls)),
    url(r'^lifestream/', include(hyperbola.lifestream.urls)),
    url(r'^404.html$', NotFound404View.as_view()),
]

if settings.ENVIRONMENT in ['production', 'dev']:
    # only enable admin urls in production
    urlpatterns += [
        url(r'^ssb/', include(django.contrib.admin.site.urls)),
        url(r'^ssb/doc/', include(django.contrib.admindocs.urls)),
    ]
