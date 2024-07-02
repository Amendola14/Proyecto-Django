from django.contrib import admin
from .models import Producto, Marca, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'numero', 'marca', 'precio', 'categoria', 'imagen')
    list_filter = ['activo', 'categoria']
    search_fields = ['titulo']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca)
admin.site.register(Categoria)
