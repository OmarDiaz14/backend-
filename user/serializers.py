from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','first_name','last_name','cargo','unidad_admi']

    

