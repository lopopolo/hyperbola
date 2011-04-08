'''
Created on Apr 8, 2011

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('hyperbola_django.jamjam.views',
    (r'^station/$', 'station_list'),
    (r'^(?i)station/(?P<id>[WK][a-z][a-z][a-z])/$', 'station'),
)
