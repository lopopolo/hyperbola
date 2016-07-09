import itertools
from collections import namedtuple

from django.http import Http404
from django.shortcuts import render
from sendfile import sendfile

from hyperbola.contact.models import (
    AboutMe, EmailContact, IMContact, PhoneContact, Resume, WebContact,
)

ResumeTemplateType = namedtuple("ResumeTemplateType", "display_name url")


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

    # Resume is always last
    try:
        latest_resume = Resume.objects.only("date").latest("date")
        resume_dto = ResumeTemplateType(
            latest_resume.display_name,
            request.build_absolute_uri(latest_resume.get_absolute_url())
        )
    except Resume.DoesNotExist:
        resume_dto = None

    return render(request, "contact_base.html", {
        "name": "Ryan Lopopolo",
        "contacts": all_contacts,
        "resume": resume_dto,
        "about": about,
    })


def resume(request):
    try:
        newest = Resume.objects.latest("date")
        return sendfile(request, newest.resume.path)
    except Resume.DoesNotExist:
        raise Http404
