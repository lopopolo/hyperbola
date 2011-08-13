from django.conf.urls.defaults import *

urlpatterns = patterns('hyperbola.frontpage.views',
  (r'^$', 'index'),
)
