# Generated by Django 2.2.4 on 2019-12-03 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0003_auto_20191203_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='contadorFotos',
        ),
    ]