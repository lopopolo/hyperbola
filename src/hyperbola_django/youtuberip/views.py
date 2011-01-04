# Create your views here.
from settings import *
from os import system

def video(request, id):
    system(DL_CMD + id + ' ' + YOUTUBE_URL + id)
    system(FFMPEG_CMD.replace('FILENAME', id))
    system('mv %s.mp3 %s' % (id, MP3_DIR))