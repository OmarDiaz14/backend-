from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    cargo = models.CharField(max_length=150, null= True, blank= True)
    unidad_admi = models.CharField(max_length=150, null= True, blank= True)
    