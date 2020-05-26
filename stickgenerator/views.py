from django.shortcuts import render
from stickergen.settings import STATICFILES_DIRS
import datetime
from calendar import monthrange
from .effects import effect
from .effects import add_effect
from .effects import reset
from .models import Image
from .models import Effect
import matplotlib.pyplot as plt
import numpy as np
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html')
    # last argument is a dict of custom values (context)


def stats_view(request, *args, **kwargs):
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    days = monthrange(current_year, current_month)[1]
    stickers_per_month = list(Image.objects.filter(created_on__month=current_month, created_on__year=current_year).values_list('created_on'))
    num_of_stikers = list()
    for day in range(1, days+1):
        num_of_stikers.append(stickers_per_month.count((datetime.date(current_year, current_month, day),)))
    path_to_stats = "stats.png"
    plt.figure(figsize=(25, 15))
    plt.bar(range(1, days+1), num_of_stikers, width=0.5)
    plt.xticks(range(1, days+1), fontsize=24)
    plt.yticks(range(0, max(num_of_stikers), 2), fontsize=24)
    plt.xlabel("days of month", fontsize=24)
    plt.ylabel("number of stickers", fontsize=24)
    plt.savefig(STATICFILES_DIRS[0] + "/" + path_to_stats)
    context = {
        "path": path_to_stats
    }
    return render(request, 'stats.html', context)


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
