import itertools

from django.http import Http404, StreamingHttpResponse
from django.shortcuts import render

from .models import (
    AboutMe, EmailContact, IMContact, PhoneContact, Resume, WebContact,
)


def index(request):
    try:
        about = AboutMe.objects.latest("pk")
    except AboutMe.DoesNotExist:
        about = None

    contact_infos = itertools.chain(
        EmailContact.objects.all(), PhoneContact.objects.all(),
        WebContact.objects.all(), IMContact.objects.all()
    )

    all_contacts = sorted(contact_infos, key=lambda k: k.type.display_order)

    try:
        newest = Resume.objects.latest("date")
    except Resume.DoesNotExist:
        newest = None

    return render(request, "contact_base.html", {
        "name": "Ryan Lopopolo",
        "contacts": all_contacts,
        "resume": newest,
        "about": about,
    })


def resume(request):
    del request
    try:
        newest = Resume.objects.latest("date")
    except Resume.DoesNotExist:
        raise Http404
    response = StreamingHttpResponse(newest.resume, content_type="application/pdf")
    response["Content-Length"] = newest.resume.size
    return response
