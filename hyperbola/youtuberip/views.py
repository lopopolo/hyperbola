# Create your views here.
from settings import *
import subprocess
from django.shortcuts import render_to_response
from django.http import HttpResponse

import os

import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

# The YouTube API does not currently support HTTPS/SSL access.
yt_service.ssl = False


def video(request, id):
    if not os.access('%s/%s.mp3' % (MP3_DIR, id), os.F_OK):
        subprocess.call(['/home/lopopolo/hyperbola/hyperbola_django/youtuberip/youtube-dl', '-o', '/tmp/%s' % (id), '%s%s' % (YOUTUBE_URL, id)])
        ffm = FFMPEG_CMD.replace('FILENAME', '/tmp/'+id)
        ff = ffm.split()
        subprocess.call(ff)
        subprocess.call(['mv', '/tmp/%s.mp3' % (id), '%s/%s.mp3' % (MP3_DIR, id)])
    
    entry = yt_service.GetYouTubeVideoEntry(video_id=id)
    
    return render_to_response("json.html", {"id" : id,
                                           "link" : 'http://media.hyperbo.la/mp3s/%s.mp3' % (id),
                                           "title" : entry.media.title.text,
                                           "bpm" : 100,
                                           "duration" : entry.media.duration.seconds})
