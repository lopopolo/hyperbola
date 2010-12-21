'''
Created on Dec 20, 2010

@author: Ryan Lopopolo
'''
import re
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template import Library

register = Library()

TAG_BASE = "/lifestream/hashtag/"

@register.filter()
def hashtagize(blurb, linktext=None, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    print blurb
    blurb = re.sub('#(?P<tag>[^\s]+)',
                   '<a href="' + TAG_BASE + '\g<tag>/">#\g<tag></a>', 
                   esc(blurb))
    print blurb
    return mark_safe(blurb)
hashtagize.needs_autoescape = True