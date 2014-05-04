from django.conf.urls import url, patterns

from hyperbola.lifestream.syndication import (
    LatestEntriesFeed, AtomLatestEntriesFeed)


urlpatterns = patterns(
    'hyperbola.lifestream.views',
    url(r'^$', 'lifestream_index', name='lifestream-home'),
    url(r'^page/(?P<page>[1-9]\d*)/$', 'lifestream_index'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_index'),
    url(
        r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>[1-9]\d*)/$',
        'archive_index'
    ),
    url(r'^hashtag/(?P<tag>\w+)/$', 'hashtag_index'),
    url(r'^hashtag/(?P<tag>\w+)/page/(?P<page>[1-9]\d*)/$', 'hashtag_index'),
    url(r'^(?P<entry_id>\d+)/$', 'permalink'),
)

urlpatterns += patterns(
    '',
    url(r'^rss/$', LatestEntriesFeed(), name='lifestream-rss'),
    url(r'^atom/$', AtomLatestEntriesFeed(), name='lifestream-atom'),
)
