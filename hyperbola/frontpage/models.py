from django.db import models

class Blurb(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  display_order = models.IntegerField()
  display = models.BooleanField(default=True)

  class Meta:
    ordering = ['display_order']
    
  def __unicode__(self):
    return "%d - %s" % (self.display_order, self.title)

class Schedule(models.Model):
  body = models.TextField()
  display_order = models.IntegerField()
  display = models.BooleanField(default=True)

  class Meta:
    ordering = ['display_order']

  def __unicode__(self):
    return "%d - %s" % (self.display_order, self.body[:50])

