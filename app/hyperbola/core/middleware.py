import logging
import socket
import uuid

from django.http import HttpResponse, HttpResponseServerError
from django.utils.encoding import force_bytes


class FQDNMiddleware(object):
    """Inject the canonical hostname for the host that rendered the request."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.comment = force_bytes('<!-- canonical hostname: {} -->'.format(socket.getfqdn()))

    def __call__(self, request):
        response = self.get_response(request)

        if 'Content-Type' in response and 'text/html' in response['Content-Type']:
            try:
                response.content = response.content + self.comment
            except ValueError:
                pass

        return response


# https://www.ianlewis.org/en/kubernetes-health-checks-django
class HealthCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('healthz')
        self.cache_key = uuid.uuid4().hex

    def __call__(self, request):
        if request.path == '/healthz' and request.method in ['GET', 'HEAD']:
            return self.healthz(request)
        return self.get_response(request)

    def healthz(self, request):
        """Return that the server is healthy."""
        # Connect to each database and do a generic standard SQL query
        # that doesn't write any data and doesn't depend on any tables
        # being present.
        try:
            from django.db import connections
            for name in connections:
                cursor = connections[name].cursor()
                cursor.execute('SELECT 1;')
                row = cursor.fetchone()
                if row is None:
                    return HttpResponseServerError('KO: db: invalid response')
        except Exception as e:
            self.logger.exception(e)
            return HttpResponseServerError('KO: db: cannot connect to database.')

        # Do a roundtrip SET and GET on a random key/value.
        # This can effectively check if each is online.
        try:
            from django.core.cache import caches
            for cache in caches.all():
                cache_value = uuid.uuid4().hex
                cache.set(self.cache_key, cache_value)
                result = cache.get(self.cache_key)
                if result != cache_value:
                    return HttpResponseServerError('KO: cache: round trip error.')
        except Exception as e:
            self.logger.exception(e)
            return HttpResponseServerError('KO: cache: cannot connect to cache.')

        return HttpResponse('OK')
