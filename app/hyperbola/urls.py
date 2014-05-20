from django.conf.urls import patterns, include, url
from django.contrib import admin
import django.contrib.admindocs.urls

import hyperbola.contact.urls
import hyperbola.frontpage.urls
import hyperbola.lifestream.urls
from hyperbola.helpers.views import NotFound404View


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^ssb/doc/', include(django.contrib.admindocs.urls)),
    url(r'^ssb/', include(admin.site.urls)),
    url(r'^$', include(hyperbola.frontpage.urls)),
    url(r'^contact/', include(hyperbola.contact.urls)),
    url(r'^lifestream/', include(hyperbola.lifestream.urls)),
    url(r'^404.html$', NotFound404View.as_view()),
)
