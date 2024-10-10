from django.db import models

class destino_expe (models.Model):
    id_destino = models.AutoField(primary_key= True)
    destino = models.CharField(max_length=100, null= False)

class type_access (models.Model):
    id_type = models.AutoField(primary_key= True)
    type = models.CharField(max_length=100, null= False,)


class valores_docu (models.Model):
    id_valores = models.AutoField (primary_key= True )
    valores = models.CharField(max_length= 100, null= False)




class Catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key= True)
    catalogo = models.CharField(max_length=50 )
    archivo_tramite = models.DateField()
    archivo_concentracion = models.DateField()
    observaciones = models.CharField(db_column='observaciones ', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    destino_expe = models.ForeignKey('destino_expe', models.DO_NOTHING, null= False)
    type_access = models.ForeignKey('type_access', models.DO_NOTHING, null= False)
    valores_documentales = models.ForeignKey('valores_docu', models.DO_NOTHING, null= False)
    id_seccion = models.ForeignKey('cuadro.Seccion', models.DO_NOTHING, blank= False, null= True)
    id_serie = models.ForeignKey('cuadro.Series', models.DO_NOTHING,blank= False, null= True)
    id_subserie = models.ForeignKey('cuadro.SubSerie', models.DO_NOTHING,blank= True, null= True)





# Create your models here.