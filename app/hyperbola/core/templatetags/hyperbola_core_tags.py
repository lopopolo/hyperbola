import markdown as _markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from .. import make_escape_function

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def anti_spamize(email, autoescape=True):
    """
    The anti_spamize filter turns email addresses into HTML entity encoded mailto links.

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
        link=encode("mailto:{}".format(esc(email))),
        text=encode(esc(email)))
    return mark_safe(result)


@register.filter
def markdown(text):
    class EscapeHTML(_markdown.Extension):
        def extendMarkdown(self, md, md_globals):
            del md.preprocessors['html_block']
            del md.inlinePatterns['html']

    return mark_safe(_markdown.markdown(text, extensions=[EscapeHTML()]))
