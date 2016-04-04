from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import hyperbola.contact.urls
import hyperbola.frontpage.urls
import hyperbola.lifestream.urls
from hyperbola.helpers.views import NotFound404View

urlpatterns = [
    url(r'', include(hyperbola.frontpage.urls)),
    url(r'^contact/', include(hyperbola.contact.urls)),
    url(r'^lifestream/', include(hyperbola.lifestream.urls)),
    url(r'^404.html$', NotFound404View.as_view()),
]

if settings.ENVIRONMENT in ['production', 'dev']:
    # only enable admin urls in production and dev
    urlpatterns += [
        url(r'^ssb/', admin.site.urls),
    ]

if settings.ENVIRONMENT in ['dev']:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
