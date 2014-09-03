import re

from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape, escape
from django.utils.safestring import mark_safe

from hyperbola.lifestream.views import hashtag_index


register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def hashtagize(blurb, autoescape=None):
    """
    Use this filter to turn #hashtags into links
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    def linkify(matchobj):
        tag = matchobj.group('tag')
        url = reverse(hashtag_index, args=[tag])
        leader = matchobj.group('leader') if 'leader' in matchobj.groupdict() else ''
        return '{leader}<a href="{url}">#{tag}</a>'.format(leader=leader, url=url, tag=tag)

    result = re.sub(r'(?P<leader>(^|\s))#(?P<tag>\w+)', linkify, esc(blurb))
    return mark_safe(result)
