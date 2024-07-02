import datetime
from django.shortcuts import render
from venta.models import Venta, Cantidad_productos
from carrito.Carro import Carro
from catalogo.models import Producto

def registro_venta(request):
    fecha_hora_actual = datetime.datetime.now()
    
    usuario_activo = request.user
    
    venta_nueva = Venta(fecha=fecha_hora_actual,usuario=usuario_activo)
    venta_nueva.save()

    carro = Carro(request)
    
    for k in carro.carro:
        producto = Producto.objects.get(id=k)
        venta_nueva.producto.add(producto)


    for id in carro.carro:
        producto_consultado = Producto.objects.get(id=id)
        cantidad = carro.carro[id]['cantidad']
        cant = Cantidad_productos(producto=producto_consultado, venta=venta_nueva, cantidad=cantidad)
        cant.save()

    return render(request, 'venta_exito.html', {})