import re
from django.utils.safestring import mark_safe
from django.template import Library
from django.core.urlresolvers import reverse
from hyperbola.lifestream import views

register = Library()

def linkify(matchobj):
  url = reverse(views.tag_page, args=[matchobj.group("tag")])
  link_tag = ""
  if "leader" in matchobj.groupdict():
    link_tag += matchobj.group("leader")
  link_tag += '<a href="%s">#%s</a>' % (url, matchobj.group("tag"))
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

