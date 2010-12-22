# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *

def index(request):
    categories = Category.objects.all()
    
    structured = []
    
    for category in categories:
        cat_name = category.name
        projects = category.app_set.all()
        projects_in_this_cat = []
        for project in projects:
            p = []
            p.append(project.name)
            p.append(project.slug)
            p.append(project.description)
            
            try:
                image = project.appimage_set.get(display_order=1)
                p.append(image.image.url)
            except AppImage.DoesNotExist:
                p.append(None)
            
            projects_in_this_cat.append(p)
        structured.append((cat_name, category.slug, projects_in_this_cat))
    
    return render_to_response("index.html", {"projects" : structured})

def tag(request, tag):
    apps = Tag.objects.get(tag=tag).app_set.all()
    projects = []
    for app in apps:
        p = []
        p.append(app.name)
        p.append(app.slug)
        p.append(app.description)
        p.append(app.category.slug)
        
        try:
            image = app.appimage_set.get(display_order=1)
            p.append(image.image.url)
        except AppImage.DoesNotExist:
            p.append(None)
        
        projects.append(p)
    if projects is []:
        projects = None
    return render_to_response("tag.html", {"projects" : projects,
                                           "tag" : tag})

def app(request, category, name):
    return HttpResponse()

def category(request, category):
    return HttpResponse()