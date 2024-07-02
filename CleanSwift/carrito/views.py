from django.shortcuts import render, redirect, get_object_or_404
from .Carro import Carro
from catalogo.models import Producto

def carro_resumen(request):
    carro = Carro(request)
    request.session['cantidad'] = carro.__len__()
    return render(request, 'carro_resumen.html', {'carro': carro})

def carro_agregar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.agregar(producto)
    request.session['cantidad'] = carro.__len__()
    return redirect('productos')

def carro_aumentar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.agregar(producto)
    request.session['cantidad'] = carro.__len__()
    return redirect('carro_resumen')

def carro_disminuir(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.disminuir(producto)
    request.session['cantidad'] = carro.__len__()
    return redirect('carro_resumen')

def carro_limpiar(request):
    carro = Carro(request)
    carro.limpiar()
    request.session['cantidad'] = carro.__len__()
    return redirect('productos')

def carro_borrar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.borrar(str(producto.id))
    request.session['cantidad'] = carro.__len__()
    return redirect('carro_resumen')
