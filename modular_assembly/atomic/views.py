from django.http import HttpResponse

def view(request):
    return HttpResponse("This is a generic view")