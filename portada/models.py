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
    seccion = models.ForeignKey('cuadro.Seccion', models.DO_NOTHING, null= True, blank= True)
    serie = models.ForeignKey('cuadro.Series', models.DO_NOTHING, null= True, blank=True)
    subserie = models.ForeignKey('cuadro.Subserie', models.DO_NOTHING, null = True, blank=True )
    ficha = models.ForeignKey('ficha_tecnica.FichaTecnica', models.DO_NOTHING, null= True, blank= True )
    catalogo = models.ForeignKey('catalogo.Catalogo', models.DO_NOTHING, null= True)


    @property
    def  soporte_docu(self):
        if self.ficha:  
            return self.ficha.soporte_docu
        else:
            return None
        
    @property 
    def destino(self):
        if self.catalogo:
            return self.catalogo.destino
        else:
            return None
    @property
    def valor(self):
        if self.catalogo:
            return self.catalogo.valor
        else:
            return None
        
    @property
    def type(self):
        if self.catalogo:
            return self.catalogo.type
        else:
            return None