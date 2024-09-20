from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import FichaTecSerializer
from .models import FichaTecnica


# Create your views here.

class FichaTecViewSet(viewsets.ModelViewSet):
    queryset = FichaTecnica.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FichaTecSerializer


