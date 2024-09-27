#from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import  GuiaSerializer
from .models import GuiaDocu


# Create your views here.

class GuiaViewSet(viewsets.ModelViewSet):
    queryset = GuiaDocu.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GuiaSerializer