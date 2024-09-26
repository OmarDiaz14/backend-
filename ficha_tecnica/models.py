from django.db import models
from cuadro.models import Seccion, Series, SubSerie

# Create your models here.

class FichaTecnica(models.Model):
    id_ficha = models.CharField(max_length=150, primary_key = True)
    area_resguardante = models.CharField(max_length= 250)
    area_intervienen = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    soporte_docu = models.CharField(max_length=250)
    id_seccion = models.ForeignKey('cuadro.Seccion', models.DO_NOTHING,  null=True, blank=False)
    id_serie = models.ForeignKey('cuadro.Series', models.DO_NOTHING, null=True, blank=False)
    id_subserie = models.ForeignKey('cuadro.SubSerie', models.DO_NOTHING, null=True, blank=False)



