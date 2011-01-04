# Create your views here.
from settings import *
from os import system
from django.shortcuts import render_to_response
from django.http import HttpResponse

def video(request, id):
    system(DL_CMD + id + ' ' + YOUTUBE_URL + id)
    system(FFMPEG_CMD.replace('FILENAME', id))
    system('mv %s.mp3 %s' % (id, MP3_DIR))
    return HttpResponse('http://media.hyperbo.la/mp3s/%s.mp3' % (id))