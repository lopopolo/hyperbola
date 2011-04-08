'''
Created on Apr 8, 2011

@author: Ryan Lopopolo
'''
from django.contrib import admin
from models import Station, Song

class SongAdmin(admin.ModelAdmin):
    date_hierarchy = 'air_time'
    list_display = ('__unicode__', 'air_time')


admin.site.register(Station)
admin.site.register(SongAdmin)
