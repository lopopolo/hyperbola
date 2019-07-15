import bleach
from bleach_whitelist.bleach_whitelist import all_styles, markdown_attrs, markdown_tags
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown import markdown as markdown_render

from .. import make_escape_function

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def anti_spamize(email, autoescape=True):
    """
    Filter to turn email addresses into HTML entity encoded mailto links.

    Args:
        email (str): The email to encode. The encoded email will be the link's
            href value and text.
        autoescape (bool): Whether or not this template tag should escape blurb
            before inserting hashtag link markup.

    """
    esc = make_escape_function(autoescape)

    def encode(value):
        return "".join(["&#x{:x};".format(ord(char)) for char in value])

    result = '<a href="{link}">{text}</a>'.format(
        link=encode("mailto:{}".format(esc(email))), text=encode(esc(email))
    )
    return mark_safe(result)


@register.simple_tag(takes_context=True)
def fullurl(context, path):
    request = context["request"]
    return request.build_absolute_uri(path)


@register.filter
def markdown(text):
    tags = markdown_tags + ["pre"]
    attrs = {**markdown_attrs, **{"div": ["class"], "span": ["class"], "img": ["class", "srcset"]}}
    ext_opts = {"codehilite": {"css_class": "syntax"}}
    return mark_safe(
        bleach.clean(
            markdown_render(
                text, extensions=["codehilite", "fenced_code"], extension_configs=ext_opts
            ),
            tags,
            attrs,
            all_styles,
        )
    )
