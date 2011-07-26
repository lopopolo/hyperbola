'''
Created on Dec 15, 2010

@author: Ryan Lopopolo
'''
from django.contrib import admin
from models import EmailContact, PhoneContact, WebContact, IMContact, Resume, ContactType, AboutMe
    
class TypeAdmin(admin.ModelAdmin):
    fields = ["display_order", "type"]

admin.site.register(EmailContact)
admin.site.register(PhoneContact)
admin.site.register(WebContact)
admin.site.register(IMContact)
admin.site.register(Resume)
admin.site.register(ContactType, TypeAdmin)
admin.site.register(AboutMe)
