from django.conf.urls import patterns, include
from django.views.generic import TemplateView

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
    (r'^404.html$', TemplateView.as_view(template_name='404.html')),
)
