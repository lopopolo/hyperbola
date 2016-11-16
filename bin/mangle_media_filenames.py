#!/usr/bin/env python

import os
import shutil

import django
from django.conf import settings

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hyperbola.settings')
    django.setup()

    from hyperbola.core import make_upload_to
    from hyperbola.contact.models import AboutMe, Resume
    from hyperbola.lifestream.models import LifeStreamPicture

    lifestream_upload_to = make_upload_to('lifestream')
    for picture in LifeStreamPicture.objects.all():
        mangled_name = lifestream_upload_to(picture, picture.picture.name)
        old_path = os.path.join(settings.MEDIA_ROOT, picture.picture.name)
        new_path = os.path.join(settings.MEDIA_ROOT, mangled_name)
        print('{} -> {}'.format(old_path, new_path))
        os.rename(old_path, new_path)
        picture.picture.name = mangled_name
        picture.save()
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'lifestream/photos'), ignore_errors=True)

    resume_upload_to = make_upload_to('resume')
    for resume in Resume.objects.all():
        mangled_name = resume_upload_to(resume, resume.resume.name)
        old_path = os.path.join(settings.MEDIA_ROOT, resume.resume.name)
        new_path = os.path.join(settings.MEDIA_ROOT, mangled_name)
        print('{} -> {}'.format(old_path, new_path))
        os.rename(old_path, new_path)
        resume.resume.name = mangled_name
        resume.save()
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'resume/2012'), ignore_errors=True)
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'resume/2013'), ignore_errors=True)
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'resume/2014'), ignore_errors=True)
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'resume/2015'), ignore_errors=True)
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'resume/2016'), ignore_errors=True)

    about_upload_to = make_upload_to('about')
    for about in AboutMe.objects.all():
        mangled_name = about_upload_to(about, about.photo.name)
        old_path = os.path.join(settings.MEDIA_ROOT, about.photo.name)
        new_path = os.path.join(settings.MEDIA_ROOT, mangled_name)
        print('{} -> {}'.format(old_path, new_path))
        os.rename(old_path, new_path)
        about.photo.name = mangled_name
        about.save()
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'about/photo'), ignore_errors=True)
