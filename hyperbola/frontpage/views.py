from models import *
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
  all_blurbs = Blurb.objects.all()
  blurbs = [(b.title, b.blurb) for b in all_blurbs]

  return render_to_response("frontpage.html", { "blurbs" : blurbs })
