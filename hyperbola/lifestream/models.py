from django.db import models


class LifeStreamItem(models.Model):
    pub_date = models.DateTimeField(
        auto_now=True,
        editable=False,
        db_index=True
    )
    blurb = models.CharField(max_length=200)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
            "hyperbola.lifestream.views.permalink",
            args=[str(self.id)])

    def __unicode__(self):
        return "{0} - {1}".format(self.pk, self.blurb[:50])

    class Meta:
        ordering = ["-pub_date"]


class LifeStreamPicture(LifeStreamItem):
    picture = models.ImageField(upload_to="lifestream/photos/%Y/%m/%d/%H-%M/")
