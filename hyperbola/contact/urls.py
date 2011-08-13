from django.conf.urls.defaults import *

urlpatterns = patterns('hyperbola.contact.views',
  (r'^$', 'index'),
  (r'^resume/$', 'resume'),
)
