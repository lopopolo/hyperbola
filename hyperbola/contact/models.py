from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

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
  value = models.URLField(verify_exists=False, max_length=200)

class IMContact(Contact):
  value = models.CharField(max_length=100)

class Resume(models.Model):
  resume = models.FileField(upload_to="resume")
  date = models.DateField(auto_now=True)

  def __unicode__(self):
    return "version %s as of %s" % (self.id, self.date)

class AboutMe(models.Model):
  photo = models.ImageField(upload_to="about/photo")
  blurb = models.TextField()

  def __unicode__(self):
    return "%s..." % self.blurb[:50]

