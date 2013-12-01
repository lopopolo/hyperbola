# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from models import *

class ContactGroup(object):
  def __init__(self, title, display_order=None):
    self.title = title
    self.display_order = display_order
    self.contacts = []

  def add_contact(self, contact):
    self.contacts.append(contact)

class ContactDTO(object):
  def name(self):
    pass
  def value(self):
    pass
  def is_link(self):
    return False
  def link_text(self):
    return None
  def is_email(self):
    return False

class EmailDTO(ContactDTO):
  def __init__(self, title, email):
    self.title = title
    self.email = email
  def name(self):
    return self.title
  def value(self):
    return self.email
  def is_email(self):
    return True

class PhoneDTO(ContactDTO):
  def __init__(self, title, phone):
    self.title = title
    self.phone = phone
  def name(self):
    return self.title
  def value(self):
    return self.phone

class InstantMessageDTO(ContactDTO):
  def __init__(self, title, nick):
    self.title = title
    self.nick = nick
  def name(self):
    return self.title
  def value(self):
    return self.nick

class WebDTO(ContactDTO):
  def __init__(self, title, url):
    self.title = title
    self.url = url
  def name(self):
    return self.title
  def value(self):
    return self.url
  def is_url(self):
    return True
  def link_text(self):
    return self.url

class ResumeDTO(ContactDTO):
  def __init__(self, date, url, request):
    self.date = date
    self.url = url
    self.request = request
  def name(self):
    return "As of {0}".format(self.date.strftime("%b %d %Y"))
  def value(self):
    return self.url
  def is_url(self):
    return True
  def link_text(self):
    return self.request.build_absolute_uri(self.url)


def index(request):
  all_email = EmailContact.objects.all()
  all_phone = PhoneContact.objects.all()
  all_web = WebContact.objects.all()
  all_im = IMContact.objects.all()
  contact_categories = ContactType.objects.all()
  all_contacts = { category : ContactGroup(category.type, category.display_order) for category in contact_categories }
  for email in all_email:
    all_contacts[email.type].add_contact(EmailDTO(email.name, email.value))
  for phone in all_phone:
    all_contacts[phone.type].add_contact(PhoneDTO(phone.name, phone.value))
  for web in all_web:
    all_contacts[web.type].add_contact(WebDTO(web.name, web.value))
  for im in all_im:
    all_contacts[im.type].add_contact(InstantMessageDTO(im.name, im.value))
  # prepare to ship to view
  sorted_contact_groups = sorted(all_contacts.values(), key=lambda k: k.display_order)
  filtered_contact_groups = [cg for cg in sorted_contact_groups if len(cg.contacts) > 0]
  # Resume is always last
  if Resume.objects.count() > 0:
    resume_contact_group = ContactGroup(u"R\u00E9sum\u00E9")
    latest_resume = Resume.objects.latest("date")
    resume_link = reverse(resume, args=[])
    resume_contact_group.add_contact(ResumeDTO(latest_resume.date, resume_link, request=request))
    filtered_contact_groups.append(resume_contact_group)

  return render_to_response("contact_base.html",
      { "name" : "Ryan Lopopolo", "contacts" : filtered_contact_groups,
        "about" : about() })

def about():
  about_me = None
  if AboutMe.objects.count() > 0:
    newest = AboutMe.objects.latest("id")
    about_me = newest
  return about_me

def resume(request):
  if Resume.objects.count() > 0:
    newest = Resume.objects.latest("date")
    response = HttpResponse(mimetype="application/pdf")
    response["X-Accel-Redirect"] = "/media/" + newest.resume.name #nginx
    return response
  else:
    raise Http404

