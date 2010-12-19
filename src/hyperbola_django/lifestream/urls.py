'''
Created on Dec 18, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns
from hyperbola_django.lifestream.syndication import *

urlpatterns = patterns('lifestream.views',
    (r'^$', 'page', {"page_num" : 1}),
    (r'^page/(?P<page_num>\d+)/$', 'page'),
    (r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', 'archive'),
    (r'^(?P<id>\d+)/$', 'permalink'),
)

urlpatterns += patterns('',
    (r'^rss/$', LatestEntriesFeed()),
    (r'^atom/$', AtomLatestEntriesFeed()),
)