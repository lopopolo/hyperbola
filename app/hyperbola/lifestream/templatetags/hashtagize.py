import re

from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from hyperbola.lifestream.views import hashtag_index


register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def hashtagize(blurb, autoescape=True):
    """The hashtagize filter turns #hashtags in blurb into links.

    Args:
        blurb: The lifestream entry to scan for #hashtags
        autoescape: Whether or not this template tag should escape blurb
            before inserting hashtag link markup.
    """
    if autoescape:
        def esc(x): return conditional_escape(x)
    else:
        def esc(x): return x

    def linkify(matchobj):
        tag = matchobj.group('tag')
        url = reverse(hashtag_index, args=[tag])
        if 'leader' in matchobj.groupdict():
            leader = matchobj.group('leader')
        else:
            leader = ''
        return '{leader}<a href="{url}">#{tag}</a>'.format(leader=leader,
                                                           url=url, tag=tag)

    result = re.sub(r'(?P<leader>(^|\s))#(?P<tag>\w+)', linkify, esc(blurb))
    return mark_safe(result)
