'''
Created on Dec 18, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns
from hyperbola.lifestream.syndication import *

urlpatterns = patterns('hyperbola_django.lifestream.views',
  (r'^$', 'page', {"page_num" : 1}),
  (r'^page/(?P<page_num>\d+)/$', 'page'),
  (r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', 'archive'),
  (r'^(?P<id>\d+)/$', 'permalink'),
  (r'^hashtag/(?P<tag>[^\s//]+)/$', 'tag_page', {"page_num" : 1}),
  (r'^hashtag/(?P<tag>[^\s//]+)/page/(?P<page_num>\d+)/$', 'tag_page'),
)

urlpatterns += patterns('',
  (r'^rss/$', LatestEntriesFeed()),
  (r'^atom/$', AtomLatestEntriesFeed()),
)
