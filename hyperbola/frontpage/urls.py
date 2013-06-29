from django.conf.urls import *

urlpatterns = patterns('hyperbola.frontpage.views',
  (r'^$', 'index'),
)
