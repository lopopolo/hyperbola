'''
Created on Dec 18, 2010

@author: Ryan Lopopolo
'''
from django.contrib import admin
from hyperbola_django.lifestream.models import *


admin.site.register(LifeStreamItem)
admin.site.register(LifeStreamPicture)