from django.urls import path
from .views import carro_resumen, carro_agregar, carro_borrar, carro_limpiar, carro_aumentar, carro_disminuir

urlpatterns = [
    path('carro_resumen', carro_resumen, name='carro_resumen'),
    path('agregar/<int:producto_id>/', carro_agregar, name='carro_agregar'),
    path('aumentar/<int:producto_id>/', carro_aumentar, name='carro_aumentar'),
    path('disminuir/<int:producto_id>/', carro_disminuir, name='carro_disminuir'),
    path('borrar/<int:producto_id>/', carro_borrar, name='carro_borrar'),
    path('limpiar/', carro_limpiar, name='carro_limpiar'),
]
