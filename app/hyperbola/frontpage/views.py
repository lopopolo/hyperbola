from django.shortcuts import render_to_response

from hyperbola.frontpage.models import Blurb, Schedule


def index(request):
    blurbs = Blurb.objects.filter(display=True)
    schedule = Schedule.objects.filter(display=True)

    return render_to_response(
        "frontpage.html",
        {"blurbs": blurbs, "schedule": schedule}
    )