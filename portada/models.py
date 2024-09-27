from django.db import models

# Create your models here.

class portada (models.Model):
    id_expediente = models.AutoField (primary_key= True)
    num_expediente = models.CharField(max_length=150)
    asunto = models.CharField(max_length=150)
    num_legajos = models.PositiveBigIntegerField(default=0)
    num_fojas = models.PositiveBigIntegerField(default=0)
    valores_secundarios = models.CharField(max_length=150)
    fecha_apertura = models.DateField(null=False)
    fecha_cierre = models.DateField(null= True)
    archivo_tramite = models.CharField(max_length=50)
    archivo_concentracion = models.CharField(max_length=50)
    soporte_docu = models.CharField(max_length=150)
    seccion = models.ForeignKey('cuadro.Seccion', models.DO_NOTHING, null= True, blank= True)
    serie = models.ForeignKey('cuadro.Series', models.DO_NOTHING, null= True, blank=True)
    subserie = models.ForeignKey('cuadro.Subserie', models.DO_NOTHING, null = True, blank=True )


