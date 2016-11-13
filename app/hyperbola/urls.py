from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .contact import urls as contact
from .core.views import NotFound404View
from .frontpage import urls as frontpage
from .lifestream import urls as lifestream

urlpatterns = [
    url(r'', include(frontpage)),
    url(r'^contact/', include(contact)),
    url(r'^lifestream/', include(lifestream)),
    url(r'^404.html$', NotFound404View.as_view()),
]

if settings.ENVIRONMENT in ['production', 'dev']:
    # only enable admin urls in production and dev
    urlpatterns += [
        url(r'^ssb/', admin.site.urls),
    ]

if settings.ENVIRONMENT in ['dev']:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
