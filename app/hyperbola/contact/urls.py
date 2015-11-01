from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponsePermanentRedirect

from hyperbola.contact import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^resume/lopopolo.pdf$', views.resume),
    url(
        r'^resume/?$',
        lambda req: HttpResponsePermanentRedirect(reverse_lazy(views.resume))
    ),
]
