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
from django.contrib.auth.models import User, Group, AnonymousUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import ClienteRegistroForm

# Create your views here.

#--------funcion que se reutiliza para validar el usuario que accede a las vistas
def usuarioValido(request, group_name):
    user = request.user
    print(f'USUARIOVALIDO: user el usuario actual es: {user}')

    if isinstance(user, AnonymousUser):
        return True  # permite a usuarios anónimos acceder a la página

    if not user.is_authenticated:
        logout(request)
        messages.error(request, 'Usuario no autenticado.')
        return False

    if not user.groups.filter(name=group_name).exists():
        logout(request)
        messages.error(request, 'Usuario invalido.')
        return False

    return True

#--------funcion que se reutiliza para visualizar la cantidad de items en el carro de compras
def visualizarCantidadCarro(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(id_cliente=cliente, completado=False)
        items = pedido.itempedido_set.all()
        itemsCarro = pedido.get_cantidad_items_pedido
    else:
        items = []
        pedido = {'get_total_item_oferta_descontada':0, 'get_total_item':0, 'get_cantidad_items_pedido':0}
        itemsCarro = pedido['get_cantidad_items_pedido']
        
    return itemsCarro

def homeCliente(request):
    cliente=request.user
    
    print(f'cliente: {cliente}')

    usuarioValido(request, 'cliente')

    plato = Plato.objects.order_by('?').all()
    
    context = {'listaPlatos': plato, 'cliente': cliente, 'itemsCarro': visualizarCantidadCarro(request)} 
    return render(request, 'cliente/home.html', context)

def main(request):
    context={} 
    return render(request, 'cliente/main.html')

#-------------------login, logout, registrar y perfil de cliente-------------------

def loginCliente(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente')

    if request.method == 'POST':
        username = request.POST.get('usernameCliente')
        password = request.POST.get('passwordCliente')
        user = authenticate(request, username=username, password=password)

        if user is not None and usuarioValido(request, 'cliente'):
            login(request, user)
            if user.groups.filter(name='cliente').exists() == True:
                messages.success(request, f'Bienvenido {user}!')
            return redirect('perfilCliente')
        else:
            messages.error(request, 'Contraseña o usuario incorrecto, intente de nuevo.')
            return redirect('loginCliente')
    else:
        return render(request, 'cliente/login-cliente.html', {})

@login_required
def logoutCliente(request):

    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente')

    context={} 
    try:
        logout(request)
        messages.success(request, f'Se ha cerrado sesión correctamente.')
        return redirect('homeCliente')
    except:
        messages.error(request, f'Error al cerrar sesión.')
        return redirect('homeCliente')

def registrarCliente(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente')

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

#-------------------perfil de cliente-------------------

@login_required
def perfilClientes(request, mensaje=None):
    clientes = get_object_or_404(Cliente, user=request.user)

    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente')  # redirige a la página de inicio si no es un cliente

    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    repartidores = Repartidor.objects.all()
    clientes = Cliente.objects.all()

    context = {
        "listaPlatos": plato,
        "listaCategorias": categorias,
        "listaProveedores": proveedores,
        "listaRepartidores": repartidores,
        "listaClientes": clientes,
        'userCliente': request.user
    }

    if mensaje:
        context['mensaje'] = mensaje

    return render(request, 'cliente/perfil-cliente.html', context)