from django.contrib import admin
from .models import Effect
from .models import Image
# Register your models here.
# Добавить модельку в админку, где ей можно управлять (добавлять, удалять тд.)
admin.site.register(Effect)
admin.site.register(Image)