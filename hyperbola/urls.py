"""
hyperbola URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""
from django.conf import settings
from django.urls import include, path

from .contact import urls as contact
from .core.views import not_found
from .frontpage import urls as frontpage
from .lifestream import urls as lifestream
from .shortlinks import urls as shortlinks

urlpatterns = [
    path("", include(frontpage)),
    path("contact/", include(contact)),
    path("lifestream/", include(lifestream)),
    path("s/", include(shortlinks)),
    path("404.html", not_found),
] + settings.ENVIRONMENT.additional_urls
