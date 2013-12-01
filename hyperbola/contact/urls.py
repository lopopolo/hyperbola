from django.conf.urls import patterns
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect

from hyperbola.contact.views import resume

urlpatterns = patterns(
    'hyperbola.contact.views',
    (r'^$', 'index'),
    (r'^resume/lopopolo.pdf$', 'resume'),
    (r'^resume/$', lambda req: HttpResponsePermanentRedirect(reverse(resume))),
)
