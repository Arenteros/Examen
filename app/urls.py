from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('quienes/', quienes, name="quienes"),
    path('producto/', producto, name="producto"),
    path('suscripcion/', suscriptor, name="suscripcion"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path('api/', include(router.urls))


]