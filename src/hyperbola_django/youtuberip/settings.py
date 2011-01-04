'''
Created on Jan 4, 2011

@author: Ryan Lopopolo
'''

MP3_DIR = '/var/www/hyperbola/media/mp3s'

DL_CMD = './youtube-dl -o ' # video url

FFMPEG_CMD = 'ffmpeg -i "FILENAME" -f mp3 -ab 160k -ar 44100 "FILENAME.mp3"'

YOUTUBE_URL = 'http://www.youtube.com/watch?v='