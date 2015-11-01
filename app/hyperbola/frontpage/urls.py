from django.conf.urls import url

from hyperbola.frontpage import views

urlpatterns = [
    url(r'^$', views.index),
]
