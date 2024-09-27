# Generated by Django 5.1.1 on 2024-09-27 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuadro', '0004_series_id_seccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuiaDocu',
            fields=[
                ('id_guia', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('volumen', models.IntegerField()),
                ('ubicacion_fisica', models.CharField(max_length=100)),
                ('serie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuadro.series')),
            ],
        ),
    ]
