# Create your views here.
from django.shortcuts import render_to_response
from models import EmailContact, PhoneContact, WebContact, Resume, ContactType

def index(request):
    all_email = EmailContact.objects.all()
    all_phone = PhoneContact.objects.all()
    all_web = WebContact.objects.all()
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
                contacts.append((web.name, web.value))
        
        all_contacts.append((type.type, contacts))
    return render_to_response("contact_base.html", {"name" : "Ryan Lopopolo",
                                                    "contacts" : all_contacts })