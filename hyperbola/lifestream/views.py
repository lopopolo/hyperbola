import re
from collections import namedtuple
from datetime import date
from functools import wraps

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import connection
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from .models import LifeStreamItem

_hashtag_validation_regexp = re.compile(r"\W")
NUM_PER_PAGE = 20
PageLinks = namedtuple("PageLinks", "newer older")


def handle_lifestream_404(view):
    @wraps(view)
    def inner(request, *args, **kwargs):
        try:
            return view(request, *args, **kwargs)
        except Http404:
            context = {
                "content_header": "No lifestream posts were found",
                "dates": get_archive_range(),
            }
            return render(request, "lifestream_404.html", context, status=404)

    return inner


def paginate(page, objects):
    paginator = Paginator(objects, NUM_PER_PAGE)
    try:
        return paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        raise Http404


def get_archive_range():
    truncate_date = connection.ops.date_trunc_sql("month", "pub_date")

    return (
        LifeStreamItem.objects.extra(select={"month": truncate_date})
        .values("month")
        .annotate(post_count=Count("pk"))
        .order_by("-month")
    )


@handle_lifestream_404
def index(request, page=1):
    posts = LifeStreamItem.objects.all().select_related("lifestreampicture")
    if not posts.exists():
        raise Http404

    pager = paginate(page, posts)
    older = newer = None
    if pager.has_previous():
        if pager.previous_page_number() == 1:
            newer = reverse("lifestream:index")
        else:
            newer = reverse("lifestream:index_paged", args=[pager.previous_page_number()])
    if pager.has_next():
        older = reverse("lifestream:index_paged", args=[pager.next_page_number()])

    return render(
        request,
        "lifestream_paged.html",
        {
            "posts": pager,
            "dates": get_archive_range(),
            "links": PageLinks(newer=newer, older=older),
        },
    )


@handle_lifestream_404
def archive(request, year, month, page=1):
    try:
        archive_date = date(year, month, 1)
    except ValueError:
        raise Http404

    posts = LifeStreamItem.objects.select_related("lifestreampicture").filter(
        pub_date__year=archive_date.year, pub_date__month=archive_date.month
    )
    if not posts.exists():
        raise Http404

    pager = paginate(page, posts)
    older = newer = None
    if pager.has_previous():
        if pager.previous_page_number() == 1:
            newer = reverse("lifestream:archive", args=[year, month])
        else:
            newer = reverse(
                "lifestream:archive_paged", args=[year, month, pager.previous_page_number()]
            )
    if pager.has_next():
        older = reverse("lifestream:archive_paged", args=[year, month, pager.next_page_number()])

    return render(
        request,
        "lifestream_paged.html",
        {
            "content_header": "Posts from {}".format(archive_date.strftime("%B %Y")),
            "posts": pager,
            "dates": get_archive_range(),
            "links": PageLinks(newer=newer, older=older),
        },
    )


@handle_lifestream_404
def hashtag(request, tag, page=1):
    if _hashtag_validation_regexp.match(tag) is not None:
        raise Http404

    # WARNING: MySQL does not recognize standard regexp character class
    # shorthand: http://dev.mysql.com/doc/refman/5.6/en/regexp.html
    search = fr"#{tag}([^[:alnum:]]|$)"

    posts = LifeStreamItem.objects.select_related("lifestreampicture").filter(blurb__iregex=search)
    if not posts.exists():
        raise Http404

    pager = paginate(page, posts)
    older = newer = None
    if pager.has_previous():
        if pager.previous_page_number() == 1:
            newer = reverse("lifestream:hashtag", args=[tag])
        else:
            newer = reverse("lifestream:hashtag_paged", args=[tag, pager.previous_page_number()])
    if pager.has_next():
        older = reverse("lifestream:hashtag_paged", args=[tag, pager.next_page_number()])

    return render(
        request,
        "lifestream_paged.html",
        {
            "content_header": f"Results for #{tag}",
            "posts": pager,
            "dates": get_archive_range(),
            "links": PageLinks(newer=newer, older=older),
        },
    )


@handle_lifestream_404
def permalink(request, entry_id):
    try:
        post = LifeStreamItem.objects.select_related("lifestreampicture").get(pk=entry_id)
    except LifeStreamItem.DoesNotExist:
        raise Http404

    try:
        newer = post.get_next_by_pub_date().get_absolute_url()
    except LifeStreamItem.DoesNotExist:
        newer = None

    try:
        older = post.get_previous_by_pub_date().get_absolute_url()
    except LifeStreamItem.DoesNotExist:
        older = None

    return render(
        request,
        "lifestream_paged.html",
        {
            "posts": paginate(1, (post,)),
            "dates": get_archive_range(),
            "links": PageLinks(newer=newer, older=older),
        },
    )
