from django.urls import path
from .views import registro_venta

urlpatterns = [    
    path('registro_venta', registro_venta, name='venta_exitosa'),
]

