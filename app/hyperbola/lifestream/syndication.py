from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed

from hyperbola.lifestream import views
from hyperbola.lifestream.models import LifeStreamItem


class LatestEntriesFeed(Feed):
    title = "hyperbo.la lifestream microblog"

    description = (
        "Most recent posts made to Ryan Lopopolo's "
        "lifestreaming microblog."
    )

    description_template = "blurb_feed.html"

    def link(self):
        return reverse(views.index)

    def feed_url(self):
        return reverse("lifestream-rss")

    def items(self):
        return LifeStreamItem.objects.all().select_related("lifestreampicture")

    def item_title(self, item):
        return "Post #{0}".format(item.pk)

    def item_link(self, item):
        return reverse(views.permalink, args=[item.pk])


class AtomLatestEntriesFeed(LatestEntriesFeed):
    feed_type = Atom1Feed

    subtitle = LatestEntriesFeed.description

    def feed_url(self):
        return reverse("lifestream-atom")
