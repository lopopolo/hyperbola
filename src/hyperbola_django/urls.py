from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^hyperbola_django/', include('hyperbola_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^ssb/', include(admin.site.urls)),
    (r'^$', include('hyperbola_django.frontpage.urls')),
    (r'^contact/', include('hyperbola_django.contact.urls')),
    (r'^lifestream/', include('hyperbola_django.lifestream.urls')),
)
