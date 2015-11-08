from django.shortcuts import render

from hyperbola.frontpage.models import Blurb, Schedule


def index(request):
    blurbs = Blurb.objects.filter(display=True)
    schedule = Schedule.objects.filter(display=True)

    return render(request, "frontpage.html", {
            "blurbs": blurbs,
            "schedule": schedule,
        }
    )
