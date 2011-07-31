# Create your views here.
# -*- coding: latin-1 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from models import *

def index(request):
  all_email = EmailContact.objects.all()
  all_phone = PhoneContact.objects.all()
  all_web = WebContact.objects.all()
  all_im = IMContact.objects.all()
  contact_types = ContactType.objects.all()
  all_contacts = dict([(type, []) for type in contact_types])
  for email in all_email:
    all_contacts[email.type].append((email.name, email.value))
  for phone in all_phone:
    all_contacts.append[phone.type]((phone.name, phone.value))
  for web in all_web:
    all_contacts[web.type].append((web.name, '<a href="'web.value+'">'+web.value+'</a>'))
  for im in all_im:
    all_contacts[im.type].append((im.name, im.value))

  resume_as_of = Resume.objects.all()[0].date.strftime("%b %d %Y")
  all_contacts.append((u"Résumé", [(u"As of " + resume_as_of, '<a href="resume/">http://hyperbo.la/contact/resume/</a>')]))

  return render_to_response("contact_base.html",
      { "name" : "Ryan Lopopolo", "contacts" : all_contacts,
        "about" : about() })
 
def about():
  about_me = None
  if len(AboutMe.objects.all()) > 0:
    newest = AboutMe.objects.all()[0]
    about_me = (newest.photo.url, newest.blurb)
  return about_me
   
def resume(request):
  if len(Resume.objects.all()) > 0:
    newest = Resume.objects.all()[0]
    response = HttpResponse(mimetype="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="Ryan Lopopolo.pdf"'
    response['X-Sendfile'] = newest.resume.path
    return response
  else:
    raise Http404

