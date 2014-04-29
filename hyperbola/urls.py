from django.conf.urls import patterns, include
from django.contrib import admin

from hyperbola.helpers.views import NotFound404View


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^ssb/doc/', include('django.contrib.admindocs.urls')),
    (r'^ssb/', include(admin.site.urls)),
    (r'^$', include('hyperbola.frontpage.urls')),
    (r'^contact/', include('hyperbola.contact.urls')),
    (r'^lifestream/', include('hyperbola.lifestream.urls')),
    (r'^404.html$', NotFound404View.as_view()),
)
