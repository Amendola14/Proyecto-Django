from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def index(request):
    return render(request, 'index.html')

def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', context={'productos': productos, 'categorias': categorias})

def productos_filtrados(request, categoria):
    cat = Categoria.objects.get(nombre=categoria)
    productos_filtrados = Producto.objects.filter(categoria=cat.id)
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', context={'productos': productos_filtrados, 'categorias': categorias})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST['user_name']
        email = request.POST['user_email']
        tema = request.POST['user_subject']
        mensaje = request.POST['user_message']
        plantilla = render_to_string('email.html', {
            'nombre': nombre,
            'email': email,
            'tema': tema,
            'mensaje': mensaje    
        })
        enviar_correo = EmailMessage(tema, plantilla, from_email=email, to=['lautaro@lautaro.com', email, 'lautaro@lautaro.com'])
        enviar_correo.content_subtype = 'html'
        enviar_correo.fail_silently = False
        enviar_correo.send()
    return render(request, 'contacto.html')

def home(request):
    return render(request, 'home.html')
