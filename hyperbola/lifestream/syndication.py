from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from hyperbola.lifestream.models import *

class LatestEntriesFeed(Feed):
  title = "hyperbo.la lifestream microblog"
  link = "/lifestream/"
  description = "Most recent posts made to Ryan Lopopolo's lifestreaming microblog."

  def items(self):
    return LifeStreamItem.objects.order_by('-pub_date')[:5]

  def item_title(self, item):
    return "Post #%s" % (item.pk)

  def item_description(self, item):
    desc = "Text"
    try:
      item.lifestreampicture.picture.url
      desc = "Picture"
    except LifeStreamPicture.DoesNotExist:
      pass
    desc = "%s: %s" % (desc, item.blurb[:50])
    if len(item.blurb) > 50:
      desc += "..."
    return desc

  def item_link(self, item):
    return "/lifestream/%s/" % (item.pk)

class AtomLatestEntriesFeed(LatestEntriesFeed):
  feed_type = Atom1Feed
  subtitle = LatestEntriesFeed.description

