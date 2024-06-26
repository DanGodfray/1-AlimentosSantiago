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
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import ClienteRegistroForm

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
        role = request.POST.get('role')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name='cliente').exists() and role == 'cliente':
                login(request, user)
                return redirect('perfilCliente')
            elif user.groups.filter(name='proveedor').exists() and role == 'proveedor':
                login(request, user)
                return redirect('homeCliente')
            elif user.groups.filter(name='repartidor').exists() and role == 'repartidor':
                login(request, user)
                return redirect('homeCliente')
            else:
                messages.error(request, 'Usuario invalido.')
        else:
            messages.error(request, 'Contraseña o usuario invalido, intententelo mas tarde.')
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

def registrarCliente(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            proveedor_group = Group.objects.get(name='cliente') #se le asigna un grupo al momento de registrarse
            user.groups.add(proveedor_group)
            login(request, user)
            messages.success(request, 'Usuario registrados exitosamente.')
            return redirect('perfilCliente')  #se redirige a la pagina de perfil de cliente
        else:
            messages.error(request, 'Error: no se pudo registrar el usuario.')
    else:
        form = ClienteRegistroForm()

    return render(request, 'cliente/registrarse-cliente.html', {'form': form})
    
#-------------------------------fin de autenticacion de cliente

@login_required
def perfilClientes(request, mensaje=None):
    user=request.user
    
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    repartidores = Repartidor.objects.all()
    clientes = Cliente.objects.all()
    
    role = request.POST.get('role')
    user = authenticate(request, username=user.username, password=user.password)
    if user is not None:
        if user.groups.filter(name='cliente').exists() and role == 'cliente':
            login(request, user)
            return redirect('perfilCliente')
        elif user.groups.filter(name='proveedor').exists() and role == 'proveedor':
            #login(request, user)
            return redirect('homeCliente')
        elif user.groups.filter(name='repartidor').exists() and role == 'repartidor':
            #login(request, user)
            return redirect('homeCliente')
        else:
            messages.error(request, 'Usuario invalido.')
            
    else:
        #messages.error(request, 'Contraseña o usuario invalido, intententelo mas tarde.')
        #return redirect('homeCliente')    

        for p in plato:
            if not p.foto_plato:
                p.foto_plato = 'img/Ui-12-1024.webp'

        if mensaje is not None:
            context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes,'mensaje': mensaje, 'userCliente': userCliente}
            return render(request, 'cliente/perfil-cliente.html', context)
        else:
            context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes, 'userCliente': user}
            return render(request, 'cliente/perfil-cliente.html', context)


    #------aqui deberia comenzar if post para editar perfil de cliente