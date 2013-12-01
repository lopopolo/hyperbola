from django.conf.urls import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^ssb/doc/', include('django.contrib.admindocs.urls')),
    (r'^ssb/', include(admin.site.urls)),
    (r'^$', include('hyperbola.frontpage.urls')),
    (r'^contact/', include('hyperbola.contact.urls')),
    (r'^lifestream/', include('hyperbola.lifestream.urls')),
)
