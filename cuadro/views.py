from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import Seccion, Series, SubSerie, SeccionSerializer, SerieSerializer, SubSerieSerializer


# Create your views here.

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SeccionSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = [SerieSerializer]

class SubSerieViewSet(viewsets.ModelViewSet):
    queryset = SubSerie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_classes = [SubSerieSerializer]
