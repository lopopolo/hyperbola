from datetime import date
from functools import wraps

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render_to_response

from hyperbola.lifestream.models import LifeStreamItem


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


def paginate(page, objects):
    paginator = Paginator(objects, NUM_PER_PAGE)
    try:
        return paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        raise Http404


def get_archive_range():
    truncate_date = connection.ops.date_trunc_sql("month", "pub_date")

    return LifeStreamItem.objects.extra(select={"month": truncate_date}) \
        .values("month").annotate(post_count=Count("pk")).order_by("-month")


@handle_lifestream_404
def lifestream_index(request, page=1):
    posts = LifeStreamItem.objects.all().select_related('lifestreampicture')
    if not posts.exists():
        raise Http404

    return render_to_response(
        "lifestream_paged.html",
        {"posts": paginate(page, posts),
         "dates": get_archive_range()}
    )


@handle_lifestream_404
def archive_index(request, year, month, page=1):
    year = int(year)
    month = int(month)

    posts_for_month = LifeStreamItem.objects.filter(pub_date__year=year) \
        .filter(pub_date__month=month) \
        .select_related('lifestreampicture')

    if not posts_for_month.exists():
        raise Http404

    return render_to_response(
        "lifestream_archived_posts.html",
        {"posts": paginate(page, posts_for_month),
         "month": date(year, month, 1),
         "dates": get_archive_range()}
    )


@handle_lifestream_404
def hashtag_index(request, tag, page=1):
    hashedtag = r"#{0}([^A-Za-z0-9]|$)".format(tag)
    qs = LifeStreamItem.objects.filter(blurb__iregex=hashedtag) \
        .select_related('lifestreampicture')

    if not qs.exists():
        raise Http404

    return render_to_response(
        "lifestream_tag_paged.html",
        {"tag": tag,
         "posts": paginate(page, qs),
         "dates": get_archive_range()}
    )


@handle_lifestream_404
def permalink(request, entry_id):
    try:
        post = LifeStreamItem.objects.select_related('lifestreampicture') \
            .get(pk=entry_id)
    except LifeStreamItem.DoesNotExist:
        raise Http404

    try:
        newer = post.get_next_by_pub_date()
    except LifeStreamItem.DoesNotExist:
        newer = None

    try:
        older = post.get_previous_by_pub_date()
    except LifeStreamItem.DoesNotExist:
        older = None

    return render_to_response(
        "lifestream_entry.html",
        {"newer_post": newer,
         "older_post": older,
         "posts": [post],
         "dates": get_archive_range()}
    )
