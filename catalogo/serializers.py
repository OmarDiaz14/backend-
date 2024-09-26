from rest_framework import serializers
from .models import Catalogo
from cuadro.models import Seccion, Series


class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = ('catalogo','archivo_tramite','archivo_concentracion',
                  'baja','historico','reservado','publico','confidencial',
                  'contable_fiscal','administrativo','legal','observaciones',
                  'id_seccion','id_serie','id_subserie')
    
    id_seccion = serializers.PrimaryKeyRelatedField(queryset=Seccion.objects.all(), required=True)
    id_serie = serializers.PrimaryKeyRelatedField(queryset=Series.objects.all(), required=True)
    
        
