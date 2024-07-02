from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    titulo = models.CharField(max_length=99)
    numero = models.IntegerField()
    activo = models.BooleanField(default=True)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo