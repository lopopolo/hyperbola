from django.conf.urls.defaults import patterns, include
from django.conf import settings

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
    (r'^yt/', include('hyperbola_django.youtuberip.urls')),
    (r'^projects/', include('hyperbola_django.appstore.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': 'c:/webdev/hyperbola_django/src/hyperbola_django/static/'}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': 'c:/webdev/hyperbola_django/src/hyperbola_django/media/', 'show_indexes': True}),
    )

