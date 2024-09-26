from rest_framework import routers
from .views import CatalogoViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'Catalogo', CatalogoViewSet)

urlpatterns = [
    path('', include (router.urls)),
]