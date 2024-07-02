from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Producto


class Venta(models.Model):
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)

    def __repr__(self):
        return f'Venta en {self.fecha}, cliente: {self.usuario}, productos: {self.producto}'

class Cantidad_productos(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    