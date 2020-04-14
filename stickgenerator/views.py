from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>This is my Sticker Generator :)<h1>")


def home_view(request, *args, **kwargs):
    context = {
        "username": request.user,
        "code": 123,
        "products": ["paste", "soda", "joggers"]
    }
    return render(request, 'home.html', context) # last argument is a dict of custom values