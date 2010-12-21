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
    
    blurb = re.sub('(?P<space>\s)#',
                   ' \g<space>#', 
                   esc(blurb))
    
    blurb = re.sub('(?P<space>\s)#(?P<tag>[^\s]+)(?P<end_space>\s)',
                   '\g<space><a href="' + TAG_BASE + '\g<tag>/">#\g<tag></a>\g<end_space>', 
                   esc(blurb))
    blurb = re.sub('(?P<space>\s)#(?P<tag>[^\s]+)$',
                   '\g<space><a href="' + TAG_BASE + '\g<tag>/">#\g<tag></a>', 
                   blurb)
    blurb = re.sub('^#(?P<tag>[^\s]+)(?P<end_space>\s)',
                   '<a href="' + TAG_BASE + '\g<tag>/">#\g<tag></a>\g<end_space>', 
                   blurb)
    return mark_safe(blurb)
hashtagize.needs_autoescape = True
