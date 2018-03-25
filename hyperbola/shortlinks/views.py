from django.shortcuts import get_object_or_404, redirect

from .models import ShortLink


def shortlink(_request, shortlink):
    target = get_object_or_404(ShortLink, slug=shortlink)
    return redirect(target)
