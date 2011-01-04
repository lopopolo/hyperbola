# Create your views here.
from settings import *
import subprocess
from django.shortcuts import render_to_response
from django.http import HttpResponse

def video(request, id):
    subprocess.call(DL_CMD + '"' + id + '" "' + YOUTUBE_URL + id + '"')
    subprocess.call(FFMPEG_CMD.replace('FILENAME', id))
    subprocess.call('mv "%s.mp3" %s' % (id, MP3_DIR))
    return HttpResponse('http://media.hyperbo.la/mp3s/%s.mp3' % (id))