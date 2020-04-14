from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html')
    # last argument is a dict of custom values (context)


def stats_view(request, *args, **kwargs):
    return render(request, 'stats.html')


def faq_view(request, *args, **kwargs):
    return render(request, 'faq.html')