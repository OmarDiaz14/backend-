from django.db import models

class Catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key= True)
    catalogo = models.CharField(max_length=50 )
    archivo_tramite = models.DateField()
    archivo_concentracion = models.DateField()
    destino_expe = models.CharField(max_length=150,default='valor_por_defecto')
    #baja = models.BooleanField(db_comment='destino del expedinete')
    #historico = models.BooleanField(db_comment='destino del expediente')
    type_access = models.CharField(max_length= 150, default='valor_por_defecto')
    #reservado = models.BooleanField(db_comment='tipo de acceso')
    #publico = models.BooleanField(db_comment='tipo de acceso')
    #confidencial = models.BooleanField(db_comment='tipo de acceso')
    valores_documentales = models.CharField(max_length=150, default='valor_por_defecto')
    #contable_fiscal = models.BooleanField(db_column='contable/fiscal', db_comment='valores documentales')  # Field renamed to remove unsuitable characters.
    #administrativo = models.BooleanField(db_comment='valores documentales')
    #legal = models.BooleanField(db_comment='valores documentales')
    observaciones = models.CharField(db_column='observaciones ', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_seccion = models.ForeignKey('cuadro.Seccion', models.DO_NOTHING, blank= False, null= True)
    id_serie = models.ForeignKey('cuadro.Series', models.DO_NOTHING,blank= False, null= True)
    id_subserie = models.ForeignKey('cuadro.SubSerie', models.DO_NOTHING,blank= True, null= True)
# Create your models here.