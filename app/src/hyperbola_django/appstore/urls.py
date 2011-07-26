'''
Created on Dec 21, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('hyperbola_django.appstore.views',
    (r'^$', 'index'),
    (r'^tag/(?P<tag>.+)/$', 'tag'),
    (r'^(?P<category>.+)/$', 'category'),
    (r'^(?P<category>.+)/(?P<name>.+)/$', 'app'),
    
)
