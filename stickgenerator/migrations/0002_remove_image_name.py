# Generated by Django 3.0.5 on 2020-05-12 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickgenerator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]