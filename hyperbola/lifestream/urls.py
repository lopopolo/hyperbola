from django.conf.urls import url, patterns

from hyperbola.lifestream.syndication import \
    LatestEntriesFeed, AtomLatestEntriesFeed


urlpatterns = patterns(
    'hyperbola.lifestream.views',
    url(r'^$', 'page', {"page_num": 1}, name="lifestream-home"),
    (r'^page/(?P<page_num>\d+)/$', 'page'),
    (r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$',
     'archive', {"page_num": 1}),
    (r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page_num>\d+)/$',
     'archive'),
    (r'^(?P<id>\d+)/$', 'permalink'),
    (r'^hashtag/(?P<tag>\w+)/$', 'tag_page', {"page_num": 1}),
    (r'^hashtag/(?P<tag>\w+)/page/(?P<page_num>\d+)/$', 'tag_page'),
)

urlpatterns += patterns(
    '',
    url(r'^rss/$', LatestEntriesFeed(), name='lifestream-rss'),
    url(r'^atom/$', AtomLatestEntriesFeed(), name='lifestream-atom'),
)
