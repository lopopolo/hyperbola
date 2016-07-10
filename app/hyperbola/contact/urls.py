from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.index, name="contact-index"),
    url(r'^resume/lopopolo.pdf$', views.resume, name="contact-resume-pdf"),
    url(r'^resume/?$', RedirectView.as_view(pattern_name="contact-resume-pdf",
                                            permanent=True)),
]
