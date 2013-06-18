from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from hyperbola.contact.views import resume

urlpatterns = patterns('hyperbola.contact.views',
  (r'^$', 'index'),
  (r'^resume/lopopolo.pdf$', 'resume'),
  (r'^resume/$', lambda request: HttpResponsePermanentRedirect(reverse(resume))),
)
