'''
Created on Dec 21, 2010

@author: Ryan Lopopolo
'''
from django.contrib import admin
from models import *

class DemoInline(admin.TabularInline):
    model = DemoFile
    extra = 5

class ImageInline(admin.TabularInline):
    model = AppImage
    extra = 5
    max_num = 5


class AppAdmin(admin.ModelAdmin):
    inlines = [
        DemoInline,
        ImageInline
    ]



admin.site.register(App, AppAdmin)
admin.site.register(Category)
admin.site.register(Tag)
