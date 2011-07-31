'''
Created on Dec 15, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import *

urlpatterns = patterns('hyperbola_django.contact.views',
    (r'^$', 'index'),
    (r'^resume/$', 'resume'),
)
