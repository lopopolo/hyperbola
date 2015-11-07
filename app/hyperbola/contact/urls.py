from django.conf.urls import url
from django.views.generic import RedirectView

from hyperbola.contact import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^resume/lopopolo.pdf$', views.resume, name="resume-pdf"),
    url(r'^resume/?$', RedirectView.as_view(pattern_name="resume-pdf",
                                            permanent=True)),
]
