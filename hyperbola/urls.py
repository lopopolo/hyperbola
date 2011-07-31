from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Uncomment the admin/doc line below to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  (r'^ssb/', include(admin.site.urls)),
  (r'^$', include('hyperbola.frontpage.urls')),
  (r'^contact/', include('hyperbola.contact.urls')),
  (r'^lifestream/', include('hyperbola.lifestream.urls')),
)

