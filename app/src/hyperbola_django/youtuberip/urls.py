'''
Created on Jan 4, 2011

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('hyperbola_django.youtuberip.views',
    (r'^video/(?P<id>[a-zA-Z_0-9]+)/$', 'video'),
    
)