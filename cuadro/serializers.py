from rest_framework import serializers
from .models import Seccion, Series, SubSerie



class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ('id_seccion','codigo','descripcion')
        


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id_serie', 'serie', 'codigo_serie','descripcion','id_seccion')


class SubSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSerie
        fields = ('SubSerie', 'descripcion','id_serie')
