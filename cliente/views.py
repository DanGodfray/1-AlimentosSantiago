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
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ecommerce import views
from .forms import ClienteForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.

def homeCliente(request):
    cliente=request.user
    
    print(f'cliente: {cliente}')
    plato = Plato.objects.order_by('?').all()
    
    context = {'listaPlatos': plato, 'cliente': cliente} 
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
            print(f'Cliente: {cliente} autenticado')
            messages.success(request, f'Bienvenido {username}!')
            return redirect('perfilCliente')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta, vuelva a intentarlo.')
            return redirect('loginCliente')
    else:
        return render(request, 'cliente/login-cliente.html',{})

@login_required
def logoutCliente(request):
    context={} 
    try:
        logout(request)
        messages.success(request, f'Se ha cerrado sesión correctamente.')
        return redirect('homeCliente')
    except:
        messages.error(request, f'Error al cerrar sesión.')
        return redirect('homeCliente')
    
#def registrarCliente(request):
    context={} 
    if request.method == 'POST':
        #datos personales
        nombre = request.POST.get('nombreCliente')
        apellido = request.POST.get('apellidoCliente')
        email = request.POST.get('emailCliente')
        telefono = request.POST.get('telefonoCliente')
        direccion = request.POST.get('direccionCliente')
        #datos para iniciar sesion
        username = request.POST.get('usernameCliente')
        password = request.POST.get('passwordCliente')
        try:
            cliente = Cliente.objects.create_user(
                username=username,
                password=password,
                email=email,
                nombre_cliente=nombre,
                apellido_cliente=apellido,
                telefono_cliente=telefono,
                direccion_cliente=direccion
            )
            cliente.save()
            messages.success(request, f'Cliente {nombre} {apellido} registrado correctamente.')
            return redirect('loginCliente')
        except:
            messages.error(request, f'Error al registrar el cliente, vuelva a intentarlo.')
            return redirect('registrarCliente')
    else:
        return render(request, 'cliente/registrarse-cliente.html',{})    
    
def registrarCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado correctamente.')
            return redirect('loginCliente')
        else:
            messages.error(request, 'Error al registrar el cliente, vuelva a intentarlo.')
            return redirect('registrarCliente')
    else:
        form = ClienteForm()
        context = {'form': form}
        return render(request, 'cliente/registrarse-cliente.html', context)
#-------------------------------fin de autenticacion de cliente

@login_required
def perfilClientes(request, mensaje=None):
    userCliente=request.user
    
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    repartidores = Repartidor.objects.all()
    clientes = Cliente.objects.all()

    for p in plato:
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'

    if mensaje is not None:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes,'mensaje': mensaje, 'userCliente': userCliente}
        return render(request, 'cliente/perfil-cliente.html', context)
    else:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes, 'userCliente': userCliente}
        return render(request, 'cliente/perfil-cliente.html', context)


    #------aqui deberia comenzar if post para editar perfil de cliente