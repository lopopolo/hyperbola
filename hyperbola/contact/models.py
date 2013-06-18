from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
import time

# Create your models here.
# a class of contacts (ie: Work, personal)
class ContactType(models.Model):
  type = models.CharField(max_length=200, unique=True)
  display_order = models.PositiveIntegerField(unique=True)

  def __unicode__(self):
    return "%s - %s" % (self.display_order, self.type)

  class Meta:
    ordering = ['display_order']

class Contact(models.Model):
  type = models.ForeignKey(ContactType)
  name = models.CharField(max_length=200)
  value = "blank"

  def __unicode__(self):
    return self.value

  class Meta:
    abstract = True
    ordering = ['type', 'name', 'value']

class EmailContact(Contact):
  value = models.EmailField(max_length=75)

class PhoneContact(Contact):
  value = PhoneNumberField()

class WebContact(Contact):
  value = models.URLField(max_length=200)

class IMContact(Contact):
  value = models.CharField(max_length=100)

class Resume(models.Model):
  date = models.DateField(auto_now=True)

  def upload_path(instance, filename):
    return "resume/" + time.strftime("%Y/%m/%d/%H-%M/") + "lopopolo.pdf"

  resume = models.FileField(upload_to=upload_path)

  def __unicode__(self):
    return "version %s as of %s" % (self.id, self.date)

class AboutMe(models.Model):
  photo = models.ImageField(upload_to="about/photo")
  blurb = models.TextField()

  def __unicode__(self):
    return "%s..." % self.blurb[:50]

