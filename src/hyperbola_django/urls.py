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
    (r'^$', include('frontpage.urls')),
    (r'^contact/', include('contact.urls')),
    (r'^lifestream/', include('lifestream.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'c:/webdev/hyperbola_django/src/hyperbola_django/static'}),
)
