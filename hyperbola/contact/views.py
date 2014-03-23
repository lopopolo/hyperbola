# -*- coding: utf-8 -*-

from collections import namedtuple
import itertools

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

from hyperbola.contact.models import EmailContact, PhoneContact, WebContact, \
    IMContact, Resume, AboutMe


ResumeTemplateType = namedtuple("ResumeTemplateType", "display_name url")


def index(request):
    contact_infos = itertools.chain(
        EmailContact.objects.all(),
        PhoneContact.objects.all(),
        WebContact.objects.all(),
        IMContact.objects.all()
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

    return render_to_response(
        "contact_base.html", {
            "name": "Ryan Lopopolo",
            "contacts": all_contacts,
            "resume": resume_dto,
            "about": about()
        }
    )


def about():
    try:
        return AboutMe.objects.latest("pk")
    except AboutMe.DoesNotExist:
        return None


def resume(request):
    try:
        newest = Resume.objects.latest("date")
        response = HttpResponse(content_type="application/pdf")
        response["X-Accel-Redirect"] = "/media/" + newest.resume.name  # nginx
        return response
    except Resume.DoesNotExist:
        raise Http404
