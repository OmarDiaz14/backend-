# Generated by Django 5.1 on 2024-10-04 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0004_series_id_seccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subserie',
            old_name='id_serie',
            new_name='serie',
        ),
    ]
