from models import SiteNewsItem, Blurb
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    all_blurbs = Blurb.objects.all()
    blurbs = []
    for blurb in all_blurbs:
        blurbs.append((blurb.title, blurb.blurb))
    
    most_recent_news = SiteNewsItem.objects.all()[:5]
    news = []
    for recent_news in most_recent_news:
        news.append((recent_news.blurb, recent_news.link, recent_news.pub_date))
        
    return render_to_response("frontpage.html", {'blurbs' : blurbs,
                                          'news' : news})