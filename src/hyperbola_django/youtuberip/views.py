# Create your views here.
from settings import *
import subprocess
from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
def video(request, id):
    subprocess.call(['/home/lopopolo/hyperbola/hyperbola_django/youtuberip/youtube-dl', '-o', '/tmp/%s' % (id), '%s%s' % (YOUTUBE_URL, id)])
    ffm = FFMPEG_CMD.replace('FILENAME', '/tmp/'+id)
    ff = ffm.split()
    subprocess.call(ff)
    subprocess.call(['mv', '/tmp/%s.mp3' % (id), '%s/%s.mp3' % (MP3_DIR, id)])
    return HttpResponse('http://media.hyperbo.la/mp3s/%s.mp3' % (id))
