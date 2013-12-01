from django.conf.urls import patterns

urlpatterns = patterns(
    'hyperbola.frontpage.views',
    (r'^$', 'index'),
)
