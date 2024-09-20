from rest_framework import serializers
from .models import FichaTecnica


class FichaTecSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaTecnica
        fields = ('id_ficha','area_resguardante', 'area_intervienen', 'descripcion', 'soporte_docu')