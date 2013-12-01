from django.conf import settings
from django.template import TemplateSyntaxError, Variable, \
    Node, Library


register = Library()

# TODO: This is some very unreadable YOLO code
#
# I found some tricks in URLNode and url from defaulttags.py [1]
# [1]: https://code.djangoproject.com/browser/django/trunk/django/template/defaulttags.py  # NOQA


@register.tag
def value_from_settings(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError(
            "'{0}' takes at least one argument"
            " (settings constant to retrieve)".format(bits[0])
        )

    settingsvar = bits[1]
    settingsvar = settingsvar[1:-1] if settingsvar[0] == '"' else settingsvar
    asvar = None
    bits = bits[2:]

    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    if len(bits):
        raise TemplateSyntaxError(
            "'value_from_settings' didn't recognise "
            "the arguments '{1}'".format(token)
        )

    return ValueFromSettings(settingsvar, asvar)


class ValueFromSettings(Node):
    def __init__(self, settingsvar, asvar):
        self.arg = Variable(settingsvar)
        self.asvar = asvar

    def render(self, context):
        ret_val = getattr(settings, str(self.arg))
        if self.asvar:
            context[self.asvar] = ret_val
            return ''
        else:
            return ret_val
