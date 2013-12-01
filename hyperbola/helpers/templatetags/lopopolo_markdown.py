# taken from http://www.dominicrodger.com/django-markdown.html

import markdown as md

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    extensions = []
    return mark_safe(
        md.markdown(force_text(value),
                    extensions,
                    safe_mode=True)
    )
