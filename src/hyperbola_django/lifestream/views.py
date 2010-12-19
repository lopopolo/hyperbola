# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from hyperbola_django.lifestream.models import *

NUM_PER_PAGE = 20

def page(request, page_num):
    page_num = int(page_num)
    next_page = None
    prev_page = None
    if page_num > 1:
        prev_page = page_num - 1
    if NUM_PER_PAGE * page_num < len(LifeStreamItem.objects.all()):
        next_page = page_num + 1
    
    if not page_num > 0:
        raise Http404
    grab_min = (page_num-1) * NUM_PER_PAGE
    grab_max = page_num * NUM_PER_PAGE
    if grab_min < 0 or grab_min > len(LifeStreamItem.objects.all()):
        raise Http404
    
    display_posts = LifeStreamItem.objects.all()[grab_min:grab_max]
    posts = []
    for post in display_posts:
        pic = None
        try:
            pic = post.lifestreampicture.picture.url
        except LifeStreamPicture.DoesNotExist:
            print "post is not a picture"
        posts.append((post.pub_date, post.blurb, pic, post.pk))
    
    return render_to_response("lifestream_paged.html",
                              {"prev_page" : prev_page,
                               "next_page" : next_page,
                               "page" : page_num,
                               "posts" : posts,
                               "dates" : get_archive_range()})
    
month_names = {1 : "January",
          2 : 'February',
          3 : "March",
          4 : "April",
          5 : "May",
          6 : "June",
          7 : "July",
          8 : "August",
          9 : "September",
          10: "October",
          11: "November",
          12: "December"}

def get_archive_range():
    newest = LifeStreamItem.objects.all()[0].pub_date
    oldest = LifeStreamItem.objects.all()[len(LifeStreamItem.objects.all())-1].pub_date
    dates = []
    # get year range
    for year in range(newest.year, oldest.year-1, -1):
        month_min = 1
        month_max = 12
        
        if year == newest.year:
            month_max = newest.month
        if year == oldest.year:
            month_min = oldest.month
        months_in_year = []
        for month in range(month_min, month_max+1, 1):
            months_in_year.append((month, month_names[month]))
        dates.append((year, months_in_year))
    return dates

def archive(request, year, month):
    year = int(year)
    month = int(month)
    if year < 0 or year > 9999 or month < 1 or month > 12:
        raise Http404
    matches = LifeStreamItem.objects.filter(pub_date__year=year).filter(pub_date__month=month)
    posts = []
    for post in matches:
        pic = None
        try:
            pic = post.lifestreampicture.picture.url
        except LifeStreamPicture.DoesNotExist:
            print "post is not a picture"
        posts.append((post.pub_date, post.blurb, pic, post.pk))
    
    return render_to_response("lifestream_archived_posts.html",
                              {"posts" : posts,
                               "month" : month_names[month],
                               "year" : year,
                               "dates" : get_archive_range()})

def permalink(request, id):
    max_id = LifeStreamItem.objects.all()[0].pk
    min_id = LifeStreamItem.objects.all()[len(LifeStreamItem.objects.all())-1].pk
    
    
    post = get_object_or_404(LifeStreamItem, pk=id)
    pic = None
    newer = None
    older = None
    try:
        pic = post.lifestreampicture.picture.url
    except LifeStreamPicture.DoesNotExist:
        print "post is not a picture"
    if post.pk < max_id:
        newer = post.pk + 1
    if post.pk > min_id:
        older = post.pk - 1
    
    return render_to_response("lifestream_entry.html",
                              {"prev_page" : newer,
                               "next_page" : older,
                               "pub_date" : post.pub_date,
                               "blurb" : post.blurb,
                               "picture_url" : pic,
                               "pk" : post.pk,
                               "dates" : get_archive_range()})