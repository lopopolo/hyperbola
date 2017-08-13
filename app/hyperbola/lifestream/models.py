from django.db import models
from django.urls import reverse
from stdimage.models import StdImageField

from ..core import MakeUploadTo


class LifeStreamItem(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    blurb = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("lifestream:entry_permalink", args=[str(self.id)])

    def __str__(self):
        return "{} - {}".format(self.pk, self.blurb)

    class Meta:
        ordering = ["-pub_date"]


class LifeStreamPicture(LifeStreamItem):
    picture = StdImageField(upload_to=MakeUploadTo("lifestream"), variations={
        "x1": (500, 500),
        "x2": (1000, 1000),
        "x3": (1500, 1500),
    })
