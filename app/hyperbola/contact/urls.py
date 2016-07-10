from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = "contact"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^resume/lopopolo.pdf$', views.resume, name="resume_pdf"),
    url(r'^resume/?$', RedirectView.as_view(pattern_name="contact:resume_pdf", permanent=True)),
]
