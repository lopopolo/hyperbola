'''
Created on Dec 16, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('hyperbola_django.frontpage.views',
    (r'^$', 'index'),
)
