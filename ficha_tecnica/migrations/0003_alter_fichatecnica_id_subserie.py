# Generated by Django 5.1.1 on 2024-09-24 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0001_initial'),
        ('ficha_tecnica', '0002_remove_fichatecnica_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichatecnica',
            name='id_subserie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuadro.subserie'),
        ),
    ]
