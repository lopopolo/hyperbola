from django.urls import path

from . import views

app_name = "lifestream"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/<int:page>/", views.index, name="index_paged"),
    path("archive/<int:year>/<int:month>/", views.archive, name="archive"),
    path("archive/<int:year>/<int:month>/page/<int:page>/", views.archive, name="archive_paged"),
    path("hashtag/<str:tag>/", views.hashtag, name="hashtag"),
    path("hashtag/<str:tag>/page/<int:page>/", views.hashtag, name="hashtag_paged"),
    path("<int:entry_id>/", views.permalink, name="entry_permalink"),
]
