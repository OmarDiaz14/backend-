from . import views
from django.urls import path, re_path



urlpatterns = [
    re_path('login',views.login),
    re_path('register',views.register),     
    re_path('profile',views.profile),     
     

]
