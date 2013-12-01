from models import Blurb, Schedule
from django.shortcuts import render_to_response


def index(request):
    blurbs = Blurb.objects.filter(display=True)
    schedule = Schedule.objects.filter(display=True)

    return render_to_response(
        "frontpage.html",
        {"blurbs": blurbs, "schedule": schedule}
    )
