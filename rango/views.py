from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says here is the index page")

