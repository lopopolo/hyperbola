from django.db import models
from django.db.models.signals import post_save, post_delete
from hyperbola_django.contact.models import EmailContact, PhoneContact, WebContact, IMContact, Resume
from hyperbola_django.lifestream.models import *

# Create your models here.
class Blurb(models.Model):
    title = models.CharField(max_length=200)
    blurb = models.TextField()
    display_order = models.IntegerField(unique=True)
    
    class Meta:
        ordering = ['display_order']
        
    def __unicode__(self):
        return "%s - %s" % (self.display_order, self.title)
        
class SiteNewsItem(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=200, blank=True)
    blurb = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["-pub_date"]
        
    def __unicode__(self):
        return self.blurb
        

what = {EmailContact : "contact email",
            PhoneContact : "phone number",
            WebContact : "web presence",
            IMContact : "IM contact",
            Resume : "resume",
            Blurb : "site blurb",
            LifeStreamItem : "lifestream entry",
            LifeStreamPicture : "lifestream picture"}

def obj_saved(**kwargs):
    blurb = ""
    link = ""
    if kwargs['created']:
        blurb += "New %s added." % (what[kwargs['sender']])
    else:
        blurb += "%s updated." % (what[kwargs['sender']])
    if "Contact" in str(kwargs['sender']) or "Resume" in str(kwargs['sender']):
        link = "/contact/"
    elif "LifeStream" in str(kwargs['sender']):
        link = "/lifestream/" + kwargs['instance'].pk + "/"
    
    update = SiteNewsItem(blurb=blurb, link=link)
    update.save()

def obj_deleted(**kwargs):
    blurb = ""
    link = ""
    blurb += "%s deleted." % (what[kwargs['sender']])
    if "Contact" in str(kwargs['sender']) or "Resume" in str(kwargs['sender']):
        link = "/contact"
    elif "LifeStream" in str(kwargs['sender']):
        link = "/lifestream"
    
    update = SiteNewsItem(blurb=blurb, link=link)
    update.save()

post_save.connect(obj_saved, sender=EmailContact)
post_save.connect(obj_saved, sender=PhoneContact)
post_save.connect(obj_saved, sender=WebContact)
post_save.connect(obj_saved, sender=IMContact)
post_save.connect(obj_saved, sender=Blurb)
post_save.connect(obj_saved, sender=LifeStreamItem)
post_save.connect(obj_saved, sender=LifeStreamPicture)

post_delete.connect(obj_deleted, sender=EmailContact)
post_delete.connect(obj_deleted, sender=PhoneContact)
post_delete.connect(obj_deleted, sender=WebContact)
post_delete.connect(obj_deleted, sender=IMContact)
post_delete.connect(obj_deleted, sender=Blurb)
post_delete.connect(obj_deleted, sender=LifeStreamItem)
post_delete.connect(obj_deleted, sender=LifeStreamPicture)


    
    