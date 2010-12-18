'''
Created on Dec 18, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('lifestream.views',
    (r'^$', 'page', {"page_num" : 1}),
    (r'^page/(?P<page_num>\d+)/$', 'page'),
    (r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', 'archive'),
    (r'^(?P<id>\d+)/$', 'permalink'),
)