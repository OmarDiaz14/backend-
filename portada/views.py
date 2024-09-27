from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import portadaSerializer
from .models import portada
from ficha_tecnica.models import FichaTecnica

# Create your views here.



class PortadaViewSet (viewsets.ModelViewSet):
    queryset = portada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = portadaSerializer
