from rest_framework import serializers
from .models import GuiaDocu
from cuadro.models import Series


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaDocu
        fields = ('descripcion', 'volumen', 'ubicacion_fisica', 'serie')
    
    #id_serie = serializers.PrimaryKeyRelatedField(queryset=Series.objects.all(), required=True)
    extra_kwargs = {
            'serie': {'required': True}  # Se asegura de que sea obligatorio
        }
    
    def validate_serie(self, value):
        if value is None:
            raise serializers.ValidationError("El campo serie no puede estar vacío.")
        return value