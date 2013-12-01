import re

from django.core.urlresolvers import reverse
from django.template import Library
from django.utils.html import escape
from django.utils.safestring import mark_safe

from .. import views


register = Library()


def linkify(matchobj):
    url = reverse(views.tag_page, args=[matchobj.group("tag")])
    link_tag = ""
    if "leader" in matchobj.groupdict():
        link_tag += matchobj.group("leader")

    escaped_tag = escape(matchobj.group("tag"))
    link_tag += """<a href="{0}">#{1}</a>""".format(url, escaped_tag)
    return link_tag


@register.filter()
def hashtagize(blurb):
    """
    Use this filter to turn #hashtags into links
    """

    blurb = re.sub('(?P<leader>[^&])#(?P<tag>[A-Za-z0-9]+)', linkify, blurb)
    # get hashtags that start a blurb
    blurb = re.sub('^#(?P<tag>[A-Za-z0-9]+)', linkify, blurb)
    return mark_safe(blurb)
