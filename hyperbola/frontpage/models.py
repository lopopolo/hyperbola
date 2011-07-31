from django.db import models

# Create your models here.
class Blurb(models.Model):
  title = models.CharField(max_length=200)
  blurb = models.TextField()
  display_order = models.IntegerField(unique=True)

  class Meta:
    ordering = ['display_order']
    
  def __unicode__(self):
    return "%s - %s" % (self.display_order, self.title)

