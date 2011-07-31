import re
from django.utils.safestring import mark_safe
from django.template import Library

register = Library()

TAG_BASE = "/lifestream/hashtag/"

@register.filter()
def hashtagize(blurb): 
  blurb = re.sub('#(?P<tag>[A-Za-z0-9]+)',
      '<a href="' + TAG_BASE + '\g<tag>/">#\g<tag></a>',
      blurb)

  return mark_safe(blurb)

