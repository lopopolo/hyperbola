from django.conf.urls import patterns

from syndication import \
    LatestEntriesFeed, AtomLatestEntriesFeed


urlpatterns = patterns(
    'hyperbola.lifestream.views',
    (r'^$', 'page', {"page_num": 1}),
    (r'^page/(?P<page_num>\d+)/$', 'page'),
    (r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$',
     'archive', {"page_num": 1}),
    (r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page_num>\d+)/$',
     'archive'),
    (r'^(?P<id>\d+)/$', 'permalink'),
    (r'^hashtag/(?P<tag>[A-Za-z0-9]+)/$', 'tag_page', {"page_num": 1}),
    (r'^hashtag/(?P<tag>[A-Za-z0-9]+)/page/(?P<page_num>\d+)/$', 'tag_page'),
)

urlpatterns += patterns(
    '',
    (r'^rss/$', LatestEntriesFeed()),
    (r'^atom/$', AtomLatestEntriesFeed()),
)
