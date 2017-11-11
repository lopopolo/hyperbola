from django.conf.urls import url

from . import views

app_name = "lifestream"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^page/(?P<page>[1-9]\d*)/$', views.index, name="index_paged"),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive, name="archive"),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>[1-9]\d*)/$', views.archive, name="archive_paged"),
    url(r'^hashtag/(?P<tag>\w+)/$', views.hashtag, name="hashtag"),
    url(r'^hashtag/(?P<tag>\w+)/page/(?P<page>[1-9]\d*)/$', views.hashtag, name="hashtag_paged"),
    url(r'^(?P<entry_id>\d+)/$', views.permalink, name="entry_permalink"),
]
