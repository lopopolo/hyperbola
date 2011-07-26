# Create your views here.
from django.http import HttpResponse
from models import Station, Song

def station_list(request):
    stations = Station.objects.all()
    
    ret = ''
    for station in stations:
        ret += '%s<br>' % (station)
    
    return HttpResponse(ret)

def station(request, id):
    songs = Song.objects.filter(station__identifier=id)[0:3]
    
    ret = ''
    for song in songs:
        ret += '%s<br>' % (song)
    
    return HttpResponse(ret)
