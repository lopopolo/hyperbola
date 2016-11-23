import socket

from django.utils.encoding import force_bytes

_FQDN = socket.getfqdn()
_COMMENT = force_bytes('<!-- canonical hostname: {} -->'.format(_FQDN))


class FQDNMiddleware(object):
    """Inject the canonical hostname for the host that rendered the request."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response and response.content:
            content = response.content
            try:
                index = content.index(b'</body>')
                content = content[:index] + _COMMENT + content[index:]
                response.content = content
            except ValueError:
                pass

        return response
