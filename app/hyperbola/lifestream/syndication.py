from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

from .models import LifeStreamItem


class LatestEntriesFeed(Feed):
    title = "hyperbo.la lifestream microblog"

    description = "Most recent posts made to Ryan Lopopolo's lifestreaming microblog."

    description_template = "blurb_feed.html"

    @staticmethod
    def link():
        return reverse("lifestream:index")

    @staticmethod
    def feed_url():
        return reverse("lifestream:rss")

    @staticmethod
    def items():
        return LifeStreamItem.objects.all().select_related("lifestreampicture")

    def item_title(self, item):
        return "Post #{0}".format(item.pk)

    def item_link(self, item):
        return item.get_absolute_url()


class AtomLatestEntriesFeed(LatestEntriesFeed):
    feed_type = Atom1Feed

    subtitle = LatestEntriesFeed.description

    @staticmethod
    def feed_url():
        return reverse("lifestream-atom")
