from django.db import models
import os
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
# Чтобы удалить модельку нужно удалить миграции, файл БД и pycache если есть
# суперюзера тоже надо создавать снова

# Любые изменения в БД с помоью makemigrations+migrate

class Effect(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = ProcessedImageField(upload_to='effects',
                                    processors=[ResizeToFill(100, 100)],
                                    format="JPEG")

    def __str__(self):
        return self.name


class Image(models.Model):
    image = ProcessedImageField(upload_to="userpics",
                                processors=[ResizeToFill(512, 512)],
                                format="PNG",
                                blank=False)
    draft = ImageSpecField(source='image',
                           format="PNG")
    created_on = models.DateField(auto_now_add=True)
