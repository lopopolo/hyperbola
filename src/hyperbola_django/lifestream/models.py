from django.db import models

# Create your models here.

class LifeStreamItem(models.Model):
    pub_date = models.DateTimeField(auto_now=True, editable=False)
    blurb = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "%s - %s" % (self.pk, self.blurb[:50])
    
    class Meta:
        ordering = ["-pub_date"]
    
class LifeStreamPicture(LifeStreamItem):
    picture = models.ImageField(upload_to="lifestream/photos")    