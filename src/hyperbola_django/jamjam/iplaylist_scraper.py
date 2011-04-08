'''
Created on Apr 8, 2011

@author: Ryan Lopopolo
'''
import os
import sys

sys.path.append('/home/lopopolo/hyperbola/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hyperbola_django.production_settings'



import urllib
import re
from hyperbola_django.jamjam.models import Station, Song

class iplaylistScraper():
    def __init__(self, station, url):
        self.url = url
        self.station = station
        
    def get_most_recent_songs(self):
        page = urllib.urlopen(self.url)
        playlist_page = page.read()
        songs = re.findall('<td.*?class="playlist_artist".*?>(.*)</td>', playlist_page)
        
        artist_title = [remove_extra_spaces(remove_html_tags(song)).split(' - ') for song in songs]
        
        not_in_db = []
        for song in artist_title:
            if not self.is_song_in_db(song):
                not_in_db.extend(song)
            else:
                break
        not_in_db.reverse
        for artist,title in not_in_db:
            s = Song(station=self.station, title=title, artist=artist)
            s.save()
        
    def is_song_in_db(self, song):
        (artist, title) = song
        
        most_recent_song = Song.objects.filter(station=self.station)
        if len(most_recent_song) > 0:
            most_recent_song = most_recent_song[0]
        if artist == most_recent_song.artist and title == most_recent_song.title:
            return True
        else:
            return False
    
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_extra_spaces(data):
    p = re.compile(r'\s\s+')
    return p.sub(' ', data)


stations = Station.objects.all()
i = 0
while True:
    s = stations[i]
    parser = iplaylistScraper(s.identifier, s.scrape)
    parser.get_most_recent_songs()
    i = (i+1) % len(stations)

