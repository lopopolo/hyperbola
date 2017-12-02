from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('resume/lopopolo.pdf', views.resume, name='resume_pdf'),
]
