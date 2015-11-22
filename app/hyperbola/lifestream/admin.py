from django.contrib import admin

from hyperbola.lifestream.models import LifeStreamItem, LifeStreamPicture

admin.site.register(LifeStreamItem)
admin.site.register(LifeStreamPicture)
