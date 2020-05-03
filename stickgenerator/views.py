from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def home_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        new_image = request.FILES['image']
        Image.objects.create(name='unknown', image=new_image)
    return render(request, 'home.html', context)
    # last argument is a dict of custom values (context)


def stats_view(request, *args, **kwargs):
    return render(request, 'stats.html')


def faq_view(request, *args, **kwargs):
    return render(request, 'faq.html')