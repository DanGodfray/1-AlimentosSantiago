from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ecommerce.models import Categoria, Plato, Pedido
from .models import Cliente
from proveedor.models import Proveedor
from repartidor.models import Repartidor
from django.core.paginator import Paginator
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    plato = Plato.objects.all()
    context = {'listaPlatos': plato} 
    return render(request, 'cliente/home.html', context)

def main(request):
    context={} 
    return render(request, 'cliente/main.html')

#----------------------------------autenticacion de cliente
def loginCliente(request):
    context={} 
    if request.method == 'POST':
        username = request.POST.get('usernameCliente')
        password = request.POST.get('passwordCliente')
        cliente = authenticate(request, username=username, password=password)
        if cliente is not None:
            login(request, cliente)
            messages.success(request, f'Bienvenido {username}!')
            return redirect('cliente')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta, vuelva a intentarlo.')
            return redirect('loginCliente')
    else:
        return render(request, 'cliente/login-cliente.html',{})

def logoutCliente(request):
    context={} 
    logout(request)
    messages.success(request, f'Se ha cerrado sesión correctamente.')
    return redirect('home')
    
    
#-------------------------------fin de autenticacion de cliente

def perfilClientes(request, mensaje=None):
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    repartidores = Repartidor.objects.all()
    clientes = Cliente.objects.all()

    for p in plato:
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'

    if mensaje is not None:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes,'mensaje': mensaje, }
        return render(request, 'cliente/perfil-cliente.html', context)
    else:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes }
        return render(request, 'cliente/perfil-cliente.html', context)


