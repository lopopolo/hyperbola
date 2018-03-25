from django.db import models


class ShortLink(models.Model):
    target = models.URLField(max_length=200)
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return self.target

    def __str__(self):
        return '{} - {}'.format(self.slug, self.target)
