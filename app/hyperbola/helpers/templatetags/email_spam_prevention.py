from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def anti_spamize(email, autoescape=True):
    """The anti_spamize filter turns email addresses into HTML
     entity encoded mailto links.

    Args:
        email: The email to encode. The encoded email will be the link's
            href value and text.
        autoescape: Whether or not this template tag should escape blurb
            before inserting hashtag link markup.
    """
    if autoescape:

        def esc(x):
            return conditional_escape(x)
    else:

        def esc(x):
            return x

    def encode(value):
        return "".join(["&#x{0:x};".format(ord(char)) for char in value])

    result = '<a href="{link}">{text}</a>'.format(
        link=encode("mailto:{}".format(esc(email))),
        text=encode(esc(email)))
    return mark_safe(result)
