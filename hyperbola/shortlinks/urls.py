from django.urls import path

from . import views

app_name = 'shortlinks'
urlpatterns = [
    path('<slug:shortlink>', views.shortlink, name='shortlink'),
]
