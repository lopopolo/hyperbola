from django.db import models


class Blurb(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    display_order = models.IntegerField()
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        display = ""
        if self.display:
            display = "[DISPLAY]"
        return " ".join([display, "{} - {}".format(self.display_order, self.title)])


class Schedule(models.Model):
    body = models.TextField()
    display_order = models.IntegerField()
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        display = ""
        if self.display:
            display = "[DISPLAY]"
        return " ".join([display, "{} - {:.80} ...".format(self.display_order, self.body)])
