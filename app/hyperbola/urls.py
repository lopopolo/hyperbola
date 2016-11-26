from django.conf import settings
from django.conf.urls import include, url

from .contact import urls as contact
from .core.views import NotFound404View, ReadinessCheckView
from .frontpage import urls as frontpage
from .lifestream import urls as lifestream

urlpatterns = [
    url(r'', include(frontpage)),
    url(r'^contact/', include(contact)),
    url(r'^lifestream/', include(lifestream)),
    url(r'^healthz$', ReadinessCheckView.as_view()),
    url(r'^404.html$', NotFound404View.as_view()),
] + settings.ENVIRONMENT.additional_urls
