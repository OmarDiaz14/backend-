# Generated by Django 5.1.1 on 2024-09-25 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='id_seccion',
            field=models.ForeignKey(blank=True, db_column='seccion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuadro.seccion'),
        ),
        migrations.AddField(
            model_name='subserie',
            name='id_serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuadro.series'),
        ),
    ]
