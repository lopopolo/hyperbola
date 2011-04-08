'''
Created on Apr 8, 2011

@author: Ryan Lopopolo
'''
from django.contrib import admin
from models import Station, Song


admin.site.register(Station)
admin.site.register(Song)
