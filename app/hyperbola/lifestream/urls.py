from django.conf.urls import url

from hyperbola.lifestream import views
from hyperbola.lifestream.syndication import (
    AtomLatestEntriesFeed, LatestEntriesFeed,
)

urlpatterns = [
    url(r'^$', views.index, name='lifestream-index'),
    url(r'^page/(?P<page>[1-9]\d*)/$', views.index,
        name='lifestream-index-paged'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive,
        name='lifestream-archive'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>[1-9]\d*)/$',
        views.archive, name='lifestream-archive-paged'),
    url(r'^hashtag/(?P<tag>\w+)/$', views.hashtag, name='lifestream-hashtag'),
    url(r'^hashtag/(?P<tag>\w+)/page/(?P<page>[1-9]\d*)/$',
        views.hashtag, name='lifestream-hashtag-paged'),
    url(r'^(?P<entry_id>\d+)/$', views.permalink,
        name='lifestream-entry-permalink'),
]

urlpatterns += [
    url(r'^rss/$', LatestEntriesFeed(), name='lifestream-rss'),
    url(r'^atom/$', AtomLatestEntriesFeed(), name='lifestream-atom'),
]
