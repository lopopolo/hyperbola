# Create your views here.
from settings import *
import subprocess
from django.shortcuts import render_to_response
from django.http import HttpResponse

def video(request, id):
    subprocess.call(['./youtube-dl', '-o', '"%s"' % (id), '"%s%s"' % (YOUTUBE_URL, id)])
    ffm = FFMPEG_CMD.replace('FILENAME', id)
    ff = ffm.split()
    subprocess.call(ff)
    subprocess.call(['mv', '"%s.mp3" %s' % (id, MP3_DIR)])
    return HttpResponse('http://media.hyperbo.la/mp3s/%s.mp3' % (id))