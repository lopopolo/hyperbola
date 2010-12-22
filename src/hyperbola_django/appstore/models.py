from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class App(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=200  )
    slug = models.SlugField(unique=True)
    description = models.TextField()
    download = models.FileField(upload_to="appstore/download", blank=True)
    tags = models.ManyToManyField('Tag')
    
    def __unicode__(self):
        return "%s - %s" % (self.category, self.name)
    
    class Meta:
        ordering = ('category', 'name',)
        
class DemoFile(models.Model):
    app = models.ForeignKey('App')
    file = models.FileField(upload_to="appstore/demo")
    is_index = models.BooleanField()
    
    def __unicode__(self):
        return "%s - %s" % (self.app, self.file)
    
class AppImage(models.Model):
    app = models.ForeignKey('App')
    image = models.ImageField(upload_to="appstore/images")
    display_order = models.PositiveIntegerField()
    
    def __unicode__(self):
        return "%s - %s: %s" % (self.app, self.display_order, self.image)
    
    class Meta:
        ordering = ('app', 'display_order',)

class Tag(models.Model):
    tag = models.SlugField(unique=True)
    
    def __unicode__(self):
        return "%s" % (self.tag)
    
    class Meta:
        ordering = ('tag',)