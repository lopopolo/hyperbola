from django.db import models

# Create your models here.

class Station(models.Model):
    title = models.CharField(max_length=200)
    identifier = models.CharField(max_length=4)
    genre = models.CharField(max_length=200)
    market = models.CharField(max_length=200)
    scraper_type = models.CharField(max_length=200)
    scrape= models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['market', 'identifier']
    
class Song(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    station = models.ForeignKey('Station')
    air_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.artist, self.title)
    
    class Meta:
        ordering = ['-air_time']
    