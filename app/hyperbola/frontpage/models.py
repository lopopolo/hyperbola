from django.db import models


class Blurb(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    display_order = models.IntegerField()
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return "{} - {}".format(self.display_order, self.title)


class Schedule(models.Model):
    body = models.TextField()
    display_order = models.IntegerField()
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return "{} - {}".format(self.display_order, self.body[:50])
