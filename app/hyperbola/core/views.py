from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView


class NotFound404View(TemplateView):
    template_name = "404.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


class HttpResponseServiceUnavailable(HttpResponse):
    status_code = 503


class ReadinessCheckView(View):
    """Simple readiness check view to determine DB connection / query."""

    @classmethod
    def get(cls, request):
        import django.db
        del request
        try:
            with django.db.connection.cursor() as c:
                c.execute("SELECT 0")
        except django.db.Error as e:
            return HttpResponseServiceUnavailable("Database health check failed")

        return HttpResponse("OK")

    head = get
