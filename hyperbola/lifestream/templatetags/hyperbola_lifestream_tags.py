import re

from django import template
from django.template.defaultfilters import stringfilter
from django.urls import reverse
from django.utils.safestring import mark_safe

from ...core import make_escape_function

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def hashtagize(blurb, autoescape=True):
    """
    Filter that turns #hashtags in blurb into links.

    Args:
        blurb (str): The lifestream entry to scan for #hashtags
        autoescape (bool): Whether or not this template tag should escape blurb
            before inserting hashtag link markup.

    """
    esc = make_escape_function(autoescape)

    def linkify(matchobj):
        tag = matchobj.group("tag")
        url = reverse("lifestream:hashtag", args=[tag])
        if "leader" in matchobj.groupdict():
            leader = matchobj.group("leader")
        else:
            leader = ""
        return f'{leader}<a href="{url}">#{tag}</a>'

    result = re.sub(r"(?P<leader>(^|\s))#(?P<tag>\w+)", linkify, esc(blurb))
    return mark_safe(result)
