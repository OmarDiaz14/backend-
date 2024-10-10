#from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import  CatalogoSerializer, DestinoSerializer,TypeSerializer,ValoresSerializer
from .models import Catalogo, destino_expe, type_access, valores_docu


# Create your views here.
class DestinoViewSet(viewsets.ModelViewSet):
    queryset = destino_expe.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DestinoSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = type_access.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TypeSerializer

class ValorViewSet(viewsets.ModelViewSet):
    queryset = valores_docu.objects.all()
    serializer_class = ValoresSerializer



class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CatalogoSerializer
# Create your views here.
