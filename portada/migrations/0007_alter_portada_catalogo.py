# Generated by Django 5.1 on 2024-10-11 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_destino_expe_type_access_valores_docu_and_more'),
        ('portada', '0006_portada_catalogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portada',
            name='catalogo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalogo.catalogo'),
        ),
    ]
