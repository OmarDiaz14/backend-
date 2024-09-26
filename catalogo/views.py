#from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import  CatalogoSerializer
from .models import Catalogo


# Create your views here.

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CatalogoSerializer
# Create your views here.
