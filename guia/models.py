from django.db import models

# Create your models here.

class GuiaDocu(models.Model):
    id_guia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    volumen = models.IntegerField()
    ubicacion_fisica = models.CharField(max_length=100)
    #id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    #id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    serie = models.ForeignKey('cuadro.Series', models.DO_NOTHING,blank= False, null= True)
    