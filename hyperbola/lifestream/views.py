from datetime import date
from functools import wraps

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render_to_response

from models import LifeStreamItem


NUM_PER_PAGE = 20


def handle_lifestream_404(view):
    @wraps(view)
    def inner(request, *args, **kwargs):
        try:
            return view(request, *args, **kwargs)
        except Http404:
            resp_404 = render_to_response(
                "lifestream_404.html",
                {"dates": get_archive_range()}
            )
            resp_404.status_code = 404
            return resp_404
    return inner


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


@handle_lifestream_404
def page(request, page_num):
    posts = LifeStreamItem.objects.all().select_related('lifestreampicture')
    if not posts.exists():
        raise Http404

    return render_to_response(
        "lifestream_paged.html",
        {"posts": paginate(page_num, posts),
         "dates": get_archive_range()}
    )


def get_archive_range():
    return LifeStreamItem.objects.dates("pub_date", "month") \
        .order_by("-pub_date")


@handle_lifestream_404
def archive(request, year, month, page_num):
    year = int(year)
    month = int(month)

    posts_for_month = LifeStreamItem.objects.filter(pub_date__year=year) \
        .filter(pub_date__month=month) \
        .select_related('lifestreampicture')

    if not posts_for_month.exists():
        raise Http404

    return render_to_response(
        "lifestream_archived_posts.html",
        {"posts": paginate(page_num, posts_for_month),
         "month": date(year, month, 1),
         "dates": get_archive_range()}
    )


@handle_lifestream_404
def permalink(request, id):
    post = post_generic = LifeStreamItem.objects.filter(pk=id)
    if not post.exists():
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


@handle_lifestream_404
def tag_page(request, page_num, tag):
    hashedtag = r"#{0}([^A-Za-z0-9]|$)".format(tag)
    qs = LifeStreamItem.objects.filter(blurb__iregex=hashedtag) \
        .select_related('lifestreampicture')

    if not qs.exists():
        raise Http404

    return render_to_response(
        "lifestream_tag_paged.html",
        {"tag": tag,
         "posts": paginate(page_num, qs),
         "dates": get_archive_range()}
    )
