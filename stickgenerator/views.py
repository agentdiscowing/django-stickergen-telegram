from django.shortcuts import render
from .effects import effect
from .effects import add_effect
from .effects import reset
from django.http import HttpResponse
from .models import Image
from .models import Effect
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html')
    # last argument is a dict of custom values (context)


def stats_view(request, *args, **kwargs):
    return render(request, 'stats.html')


def faq_view(request, *args, **kwargs):
    return render(request, 'faq.html')


def edit_view(request, *args, **kwargs):
    db_effects = Effect.objects.all()
    if request.method == 'POST':
        new_image = request.FILES['image']
        im = Image.objects.create(image=new_image)
        context = {
            'image': im,
            'effects': db_effects
        }
        return render(request, 'edit.html', context)
    if request.method == 'GET':
        eff = request.GET.get('effect', '')
        image_id = request.GET.get('image_id', '')
        im = Image.objects.get(id=int(image_id))
        if eff != "Reset":
            applied_effect = effect[eff]
            add_effect(applied_effect, im.draft.path)
        else:
            reset(im.draft.path, im.image.path)
        context = {
            'image': im,
            'effects': db_effects,
        }
        return render(request, 'edit.html', context)
