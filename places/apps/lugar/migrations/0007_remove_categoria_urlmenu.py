# Generated by Django 2.2.4 on 2019-12-05 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0006_reporte_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='urlMenu',
        ),
    ]
