from models import *
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
  blurbs = Blurb.objects.filter(display=True)
  schedule = Schedule.objects.filter(display=True)

  return render_to_response("frontpage.html",
      { "blurbs" : blurbs, "schedule" : schedule })
