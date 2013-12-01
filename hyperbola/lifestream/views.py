from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render_to_response

from hyperbola.lifestream.models import LifeStreamItem


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
    display_posts = paginate(
        page_num,
        LifeStreamItem.objects.all().select_related('lifestreampicture')
    )
    return render_to_response(
        "lifestream_paged.html",
        {"posts": display_posts,
         "dates": get_archive_range()}
    )


months = {
    1: ("01", "January"),
    2: ("02", "February"),
    3: ("03", "March"),
    4: ("04", "April"),
    5: ("05", "May"),
    6: ("06", "June"),
    7: ("07", "July"),
    8: ("08", "August"),
    9: ("09", "September"),
    10: ("10", "October"),
    11: ("11", "November"),
    12: ("12", "December"),
}


def get_archive_range():
    newest = LifeStreamItem.objects.latest('pub_date').pub_date
    oldest = LifeStreamItem.objects.earliest('pub_date').pub_date
    dates = []
    # get year range
    for year in range(newest.year, oldest.year-1, -1):
        month_min = 1
        month_max = 12

        if year == newest.year:
            month_max = newest.month

        if year == oldest.year:
            month_min = oldest.month

        dates.append((
            year,
            [months[month] for month in range(month_max, month_min-1, - 1)],
        ))

    return dates


def archive(request, year, month, page_num):
    year = int(year)
    month = int(month)
    if year < 0 or year > 9999 or month < 1 or month > 12:
        raise Http404

    posts_for_year = LifeStreamItem.objects.filter(pub_date__year=year) \
        .filter(pub_date__month=month) \
        .select_related('lifestreampicture')

    paged_posts_for_year = paginate(page_num, posts_for_year)

    return render_to_response(
        "lifestream_archived_posts.html",
        {"posts": paged_posts_for_year,
         "month": months[month][1],
         "year": year,
         "month_num": month,
         "dates": get_archive_range()}
    )


def permalink(request, id):
    post = post_generic = LifeStreamItem.objects.filter(pk=id)
    if post.count() < 1:
        raise Http404
    try:
        newer = post_generic[0].get_next_by_pub_date().pk
        post.has_previous = True
    except LifeStreamItem.DoesNotExist:
        newer = None

    try:
        older = post_generic[0].get_previous_by_pub_date().pk
        post.has_next = True
    except LifeStreamItem.DoesNotExist:
        older = None

    return render_to_response(
        "lifestream_entry.html",
        {"prev_page": newer,
         "next_page": older,
         "posts": post,
         "dates": get_archive_range()}
    )


def tag_page(request, page_num, tag):
    hashedtag = r"#{0}([^A-Za-z0-9]|$)".format(tag)
    qs = LifeStreamItem.objects.filter(blurb__iregex=hashedtag) \
        .select_related('lifestreampicture')
    matches = paginate(page_num, qs)

    return render_to_response(
        "lifestream_tag_paged.html",
        {"tag": tag,
         "posts": matches,
         "dates": get_archive_range()}
    )
