from django.conf.urls import patterns, url

urlpatterns = patterns(
    'hyperbola.frontpage.views',
    url(r'^$', 'index'),
)
