from django.shortcuts import render


def not_found(request):
    return render(request, "404.html", status=404)
