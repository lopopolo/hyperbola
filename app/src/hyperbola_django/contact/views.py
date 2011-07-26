# Create your views here.
# -*- coding: latin-1 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from models import EmailContact, PhoneContact, WebContact, IMContact, Resume, ContactType, AboutMe

def index(request):
    all_email = EmailContact.objects.all()
    all_phone = PhoneContact.objects.all()
    all_web = WebContact.objects.all()
    all_im = IMContact.objects.all()
    contact_types = ContactType.objects.all()
    all_contacts = []
    for type in contact_types:
        contacts = []
        for email in all_email:
            if email.type == type:
                contacts.append((email.name, email.value))
        for phone in all_phone:
            if phone.type == type:
                contacts.append((phone.name, phone.value))
        for web in all_web:
            if web.type == type:
                contacts.append((web.name, '<a href="'+web.value+'">'+web.value+'</a>'))
        
        for im in all_im:
            if im.type == type:
                contacts.append((im.name, im.value))
        
        all_contacts.append((type.type, contacts))
    resume_as_of = Resume.objects.all()[0].date.strftime("%b %d %Y")
    all_contacts.append((u"R�sum�", [(u"As of " + resume_as_of, '<a href="resume/">http://hyperbo.la/contact/resume/</a>')]))
    
    return render_to_response("contact_base.html", {"name" : "Ryan Lopopolo",
                                                    "contacts" : all_contacts,
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