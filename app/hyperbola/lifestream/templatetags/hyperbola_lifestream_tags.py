import re

from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from hyperbola.core import make_escape_function

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def hashtagize(blurb, autoescape=True):
    """The hashtagize filter turns #hashtags in blurb into links.

    Args:
        blurb (str): The lifestream entry to scan for #hashtags
        autoescape (bool): Whether or not this template tag should escape blurb
            before inserting hashtag link markup.
    """
    esc = make_escape_function(autoescape)

    def linkify(matchobj):
        tag = matchobj.group('tag')
        url = reverse("lifestream:hashtag", args=[tag])
        if 'leader' in matchobj.groupdict():
            leader = matchobj.group('leader')
        else:
            leader = ''
        return '{leader}<a href="{url}">#{tag}</a>'.format(leader=leader, url=url, tag=tag)

    result = re.sub(r'(?P<leader>(^|\s))#(?P<tag>\w+)', linkify, esc(blurb))
    return mark_safe(result)
