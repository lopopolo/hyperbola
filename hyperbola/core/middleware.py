import logging
import socket
import textwrap
import uuid

from django.http import HttpResponse
from django.utils.encoding import force_bytes

import hyperbola


class FQDNMiddleware:
    """Inject the canonical hostname for the host that rendered the request."""

    def __init__(self, get_response):
        self.get_response = get_response
        fqdn = socket.getfqdn()
        self.comment = force_bytes(f"<!-- FQDN: {fqdn}, VERSION: {hyperbola.__version__} -->")

    def __call__(self, request):
        response = self.get_response(request)

        if "Content-Type" in response and "text/html" in response["Content-Type"]:
            try:
                response.content = response.content + self.comment
            except ValueError:
                pass

        return response


class HttpResponseServiceUnavailable(HttpResponse):
    status_code = 503
    content_type = "text/plain"

    def __init__(self, *args, **kwargs):
        kwargs2 = kwargs.copy()
        kwargs2["content_type"] = "text/plain"
        super().__init__(*args, **kwargs2)


# https://www.ianlewis.org/en/kubernetes-health-checks-django
class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("healthz")
        self.cache_key = uuid.uuid4().hex
        self.fqdn = socket.getfqdn()

    def __call__(self, request):
        if request.path == "/healthz" and request.method in ["GET", "HEAD"]:
            return self.healthz(request)
        return self.get_response(request)

    def _response(self, *, ko=None):
        if ko is None:
            return HttpResponse(
                textwrap.dedent(
                    f"""\
                    VERSION: {hyperbola.__version__}
                    FQDN: {self.fqdn}
                    OK
                    """
                ),
                content_type="text/plain",
            )
        else:
            return HttpResponseServiceUnavailable(
                textwrap.dedent(
                    f"""\
                    VERSION: {hyperbola.__version__}
                    FQDN: {self.fqdn}
                    KO: {ko}
                    """
                )
            )

    def healthz(self, request):
        """Return that the server is healthy."""
        # Connect to each database and do a generic standard SQL query
        # that doesn't write any data and doesn't depend on any tables
        # being present.
        try:
            from django.db import connections

            for name in connections:
                cursor = connections[name].cursor()
                cursor.execute("SELECT 1;")
                row = cursor.fetchone()
                if row is None:
                    return self._response(ko="db: invalid response")
        except Exception as e:
            self.logger.exception(e)
            return self._response(ko="db: cannot connect to database")

        # Do a roundtrip SET and GET on a random key/value.
        # This can effectively check if each is online.
        try:
            from django.core.cache import caches

            caches["default"]
            if not caches.all():
                return self._response(ko="cache: no cache configured")
            for cache in caches.all():
                cache_value = uuid.uuid4().hex
                cache.set(self.cache_key, cache_value)
                result = cache.get(self.cache_key)
                if result != cache_value:
                    return self._response(ko="cache: round trip error")
        except Exception as e:
            self.logger.exception(e)
            return self._response(ko="cache: cannot connect to cache")

        return self._response()
