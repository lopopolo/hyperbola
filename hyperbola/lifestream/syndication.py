from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.feedgenerator import Atom1Feed

from models import LifeStreamItem
import views


class LatestEntriesFeed(Feed):
    title = "hyperbo.la lifestream microblog"
    link = "/lifestream/"
    description = "Most recent posts made to Ryan Lopopolo's " + \
        "lifestreaming microblog."

    def items(self):
        return LifeStreamItem.objects.all().select_related('lifestreampicture')

    def item_title(self, item):
        return "Post #%s" % (item.pk)

    def item_description(self, item):
        post = render_to_response("blurb.html", {"post": item})
        return post.content

    def item_link(self, item):
        return reverse(views.permalink, args=[item.pk])


class AtomLatestEntriesFeed(LatestEntriesFeed):
    feed_type = Atom1Feed
    subtitle = LatestEntriesFeed.description
