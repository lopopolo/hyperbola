from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hyperbola.lifestream.models import *
from hyperbola.helpers.inheritance_query_set import *

NUM_PER_PAGE = 20

def paginate(page_num, objects):
  paginator = Paginator(objects, NUM_PER_PAGE)
  try:
    return paginator.page(page_num)
  except PageNotAnInteger:
    # if page is not an integer, deliver first page
    return paginator.page(1)
  except EmptyPage:
    # If page is out of range, deliver last page
    return paginator.page(paginator.num_pages)

def page(request, page_num):
  display_posts = paginate(page_num, InheritanceQuerySet(model=LifeStreamItem).select_subclasses())
  return render_to_response("lifestream_paged.html",
      { "posts" : display_posts,
        "dates" : get_archive_range() })
    
month_names = {
    1 : "January",
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
    12: "December"
}

def get_archive_range():
  all = LifeStreamItem.objects.all()
  newest = all[0].pub_date
  oldest = all.reverse()[0].pub_date
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
    for month in range(month_max, month_min-1,- 1):
      months_in_year.append((month, month_names[month]))
    dates.append((year, months_in_year))
  return dates

def archive(request, year, month, page_num):
  year = int(year)
  month = int(month)
  if year < 0 or year > 9999 or month < 1 or month > 12:
    raise Http404
  posts = paginate(page_num, InheritanceQuerySet(model=LifeStreamItem).select_subclasses().filter(pub_date__year=year).filter(pub_date__month=month))

  return render_to_response("lifestream_archived_posts.html",
      { "posts" : posts, "month" : month_names[month], "year" : year,
        "month_num" : month, "dates" : get_archive_range() })

def permalink(request, id):
  post = InheritanceQuerySet(model=LifeStreamItem).select_subclasses().filter(pk=id)
  post_generic = LifeStreamItem.objects.filter(pk=id)
  if post.count() < 1:
    raise Http404
  try:
    newer = post_generic[0].get_next_by_pub_date().pk
  except LifeStreamItem.DoesNotExist:
    newer = None
  try:
    older = post_generic[0].get_previous_by_pub_date().pk
  except LifeStreamItem.DoesNotExist:
    older = None

  return render_to_response("lifestream_entry.html", 
      { "prev_page" : newer, "next_page" : older,
        "post" : post[0], "dates" : get_archive_range() })
    
def tag_page(request, page_num, tag):
  hashedtag = " #%s " % (tag)
  hashedtagns = " #%s" % (tag)
  hashedtagnfs = "#%s " % (tag)
  qs = InheritanceQuerySet(model=LifeStreamItem).select_subclasses()
  matches = qs.filter(blurb__contains=hashedtag) | \
      qs.filter(blurb__endswith=hashedtagns) | \
      qs.filter(blurb__startswith=hashedtagnfs)
  matches = paginate(page_num, matches)

  return render_to_response("lifestream_tag_paged.html",
      { "tag" : tag, "posts" : matches,
        "dates" : get_archive_range() })

