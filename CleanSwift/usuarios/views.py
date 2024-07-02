from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_usuario(request):
    if (request.method == "POST"):
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('productos')
        else:
            messages.success(request, "Hubo algun inconveniente al loguearse. Repetir...")
            return redirect('login')
    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('home')