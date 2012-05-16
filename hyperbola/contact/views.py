# Create your views here.
# -*- coding: latin-1 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from models import *

def index(request):
  all_email = EmailContact.objects.all()
  all_phone = PhoneContact.objects.all()
  all_web = WebContact.objects.all()
  all_im = IMContact.objects.all()
  contact_categories = ContactType.objects.all()
  all_contacts = dict([(category, []) for category in contact_categories])
  contact_order = dict([(category.display_order, category) for category in
    contact_categories])
  for email in all_email:
    all_contacts[email.type].append((email.name, email.value))
  for phone in all_phone:
    all_contacts.append[phone.type]((phone.name, phone.value))
  for web in all_web:
    all_contacts[web.type].append((web.name, '<a href="'+web.value+'">'+web.value+'</a>'))
  for im in all_im:
    all_contacts[im.type].append((im.name, im.value))
  # prepare to ship to view
  grouped_and_ordered_contacts = []
  for order in sorted(contact_order.keys()):
    category = contact_order[order]
    grouped_and_ordered_contacts.append((category.type, all_contacts[category]))
  # Resume is always last
  if Resume.objects.count() > 0:
    resume_link = reverse(resume, args=[])
    resume_as_of = Resume.objects.all()[Resume.objects.count() - 1].date.strftime("%b %d %Y")
    grouped_and_ordered_contacts.append((u"Résumé", [(u"As of " + resume_as_of,
      '<a href="'+resume_link+'">http://'+request.META['HTTP_HOST'] + resume_link+'</a>')]))

  return render_to_response("contact_base.html",
      { "name" : "Ryan Lopopolo", "contacts" : grouped_and_ordered_contacts,
        "about" : about() })

def about():
  about_me = None
  if AboutMe.objects.count() > 0:
    newest = AboutMe.objects.latest("id")
    about_me = (newest.photo.url, newest.blurb)
  return about_me

def resume(request):
  if Resume.objects.count() > 0:
    newest = Resume.objects.latest("date")
    response = HttpResponse(mimetype="application/pdf")
    response['X-Sendfile'] = newest.resume.path
    return response
  else:
    raise Http404

