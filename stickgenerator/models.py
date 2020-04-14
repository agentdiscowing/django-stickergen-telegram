from django.db import models

# Create your models here.
# Чтобы удалить модельку нужно удалить миграции, файл БД и pycache если есть
# суперюзера тоже надо создавать снова

#Любые изменения в БД с помоью makemigrations+migrate

class Effect(models.Model):
    name = models.CharField("Name", max_length=50)
    summary = models.TextField("Summary", blank=True)

    def __str__(self):
        return self.name
