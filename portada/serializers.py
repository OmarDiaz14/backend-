from rest_framework import serializers
from .models import portada
from ficha_tecnica.models import FichaTecnica
from cuadro.models import Seccion, Series 

class portadaSerializer (serializers.ModelSerializer):
    #soporte_docu = serializers.CharField(source='FichaTecnica.soporte_docu', read_only=True) 
    class Meta:
        model = portada
        fields = ['id_expediente', 'num_expediente','asunto', 'num_legajos', 'num_fojas' ,
                   'valores_secundarios','fecha_apertura', 'fecha_cierre', 'archivo_tramite', 
                   'archivo_concentracion','seccion','serie','ficha', 'soporte_docu']
    seccion = serializers.PrimaryKeyRelatedField(queryset=Seccion.objects.all(), required=True)
    serie = serializers.PrimaryKeyRelatedField(queryset=Series.objects.all(), required=True)
    ficha = serializers.PrimaryKeyRelatedField(queryset=FichaTecnica.objects.all(),required =True )