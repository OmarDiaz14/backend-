# Generated by Django 5.1.1 on 2024-09-25 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0002_series_id_seccion_subserie_id_serie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='id_seccion',
        ),
    ]
