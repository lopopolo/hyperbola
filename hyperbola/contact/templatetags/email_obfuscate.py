import codecs
import re

from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template import Library


register = Library()


@register.filter(needs_autoescape=True)
def obfuscate(email, linktext=None, autoescape=None):
    """
    Given a string representing an email address,
    returns a mailto link with rot13 JavaScript obfuscation.

    Accepts an optional argument to use as the link text;
    otherwise uses the email address itself.
    """

    if '@' in email:
        if autoescape:
            esc = conditional_escape
        else:
            esc = lambda x: x

        email = esc(re.sub(
            '@', '\\\\100',
            re.sub('\.', '\\\\056', esc(email))
        ))

        if linktext:
            linktext = esc(linktext)
        else:
            linktext = esc(email)

        # ROT13
        email = codecs.encode(email, "rot13")
        linktext = codecs.encode(linktext, "rot13")

        rotten_link = (
            """<script type="text/javascript">"""
            """\n//<![CDATA[\n"""
            """document.write("""
            """'<n uers="znvygb:{0}">{1}</n>'.replace(/[a-zA-Z]/g,"""
            """function(c) {{"""
            """return String.fromCharCode("""
            """(c<="Z"?90:122) >= (c=c.charCodeAt(0)+13)?c:c-26);}}));"""
            """\n//]]>\n"""
            """</script>"""
        ).format(email, linktext)

        return mark_safe(rotten_link)
    else:
        return conditional_escape(email)
