from django.shortcuts import get_object_or_404, render
from .models import Post


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_post.html", {"post": post})
