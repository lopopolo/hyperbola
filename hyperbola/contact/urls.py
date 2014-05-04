from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponsePermanentRedirect

from hyperbola.contact.views import resume

urlpatterns = patterns(
    'hyperbola.contact.views',
    url(r'^$', 'index'),
    url(r'^resume/lopopolo.pdf$', 'resume'),
    url(
        r'^resume/$',
        lambda req: HttpResponsePermanentRedirect(reverse_lazy(resume))
    ),
)
