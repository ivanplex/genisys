from django.http import HttpResponse


def home(request):
    return HttpResponse("Alrose @2019")
