from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    publish_date = models.DateField(auto_now_add=True)
    summary = models.TextField()
    post_markdown = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:post", args=[str(self.slug)])

    def __str__(self):
        return self.title
