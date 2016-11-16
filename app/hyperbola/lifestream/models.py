from django.core.urlresolvers import reverse
from django.db import models

from ..core import make_upload_to


class LifeStreamItem(models.Model):
    pub_date = models.DateTimeField(auto_now=True, editable=False, db_index=True)
    blurb = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("lifestream:entry_permalink", args=[str(self.id)])

    def __str__(self):
        return "{0} - {1}".format(self.pk, self.blurb[:50])

    class Meta:
        ordering = ["-pub_date"]


class LifeStreamPicture(LifeStreamItem):
    picture = models.ImageField(upload_to=make_upload_to("lifestream"))
