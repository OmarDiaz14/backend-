from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import InventarioSerializer
from .models import Inventario


# Create your views here.



class InventarioViewSet (viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InventarioSerializer
