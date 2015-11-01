from django.conf.urls import url

from hyperbola.lifestream import views
from hyperbola.lifestream.syndication import (
    LatestEntriesFeed, AtomLatestEntriesFeed)


urlpatterns = [
    url(r'^$', views.lifestream_index, name='lifestream-home'),
    url(r'^page/(?P<page>[1-9]\d*)/$', views.lifestream_index),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive_index),
    url(
        r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>[1-9]\d*)/$',
        views.archive_index
    ),
    url(r'^hashtag/(?P<tag>\w+)/$', views.hashtag_index),
    url(r'^hashtag/(?P<tag>\w+)/page/(?P<page>[1-9]\d*)/$', views.hashtag_index),
    url(r'^(?P<entry_id>\d+)/$', views.permalink),
]

urlpatterns += [
    url(r'^rss/$', LatestEntriesFeed(), name='lifestream-rss'),
    url(r'^atom/$', AtomLatestEntriesFeed(), name='lifestream-atom'),
]
