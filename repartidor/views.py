from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from cliente.models import Cliente
from ecommerce.models import Categoria, Entrega, Plato, Pedido
from repartidor.forms import RepartidorRegistroForm
from .models import Repartidor
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

# Create your views here.

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

def homeRepartidor(request):
    if not usuarioValido(request, 'repartidor'):
        return redirect('homeRepartidor')

    return render(request, 'repartidor/home-repartidor.html', {})

def loginRepartidor(request):
    if not usuarioValido(request, 'repartidor'):
        return redirect('homeRepartidor')

    if request.method == 'POST':
        username = request.POST.get('usernameRepartidor')
        password = request.POST.get('passwordRepartidor')
        user = authenticate(request, username=username, password=password)

        if user is not None and usuarioValido(request, 'repartidor'):
            login(request, user)
            if user.groups.filter(name='repartidor').exists() == True:
                messages.success(request, f'Bienvenido {user}!')
            return redirect('perfilRepartidor')
        else:
            messages.error(request, 'Contraseña o usuario incorrecto, intente de nuevo.')
            return redirect('loginRepartidor')
    else:
        return render(request, 'repartidor/login-repartidor.html', {})
    
def logoutRepartidor(request):

    if not usuarioValido(request, 'repartidor'):
        return redirect('homeRepartidor')

    context={} 
    try:
        logout(request)
        messages.success(request, f'Se ha cerrado sesión correctamente.')
        return redirect('homeRepartidor')
    except:
        messages.error(request, f'Error al cerrar sesión.')
        return redirect('homeRepartidor')

def registrarRepartidor(request):
   # if not usuarioValido(request, 'repartidor'):
    #    return redirect('homeRepartidor')
    print('antes del if')
    if request.method == 'POST':
        print('durante el if')
        form = RepartidorRegistroForm(request.POST)
        if form.is_valid():
            print('dentro del if importante')
            user = form.save()
            repartidor_group = Group.objects.get(name='repartidor') #se le asigna un grupo al momento de registrarse
            user.groups.add(repartidor_group)
            login(request, user)
            messages.success(request, 'Usuario registrados exitosamente.')
            return redirect('perfilRepartidor')  #se redirige a la pagina de perfil de cliente
        else:
            print('despues else ')
            messages.error(request, 'Error: no se pudo registrar el usuario.')
    else:
        form = RepartidorRegistroForm()

    return render(request, 'repartidor/registrarse-repartidor.html', {'form': form})

def perfilRepartidor(request, mensaje=None):
    if not usuarioValido(request, 'repartidor'):
        return redirect('homeProveedor')
    
    try:
        repartidores = Repartidor.objects.get(user=request.user)
    except Proveedor.DoesNotExist:
        messages.error(request, 'El usuario de Repartidor es incorrecto o no existe. intentelo denuevo o registrese como Repartidor.')
        return redirect('homeRepartidor') 
    
    #repartidor = Repartidor.objects.all()
     # Filtrar las entregas asignadas al repartidor
    #entregas_asignadas = Entrega.objects.filter(id_repartidor=repartidor.id_repartirdor)
    
    # Filtrar los pedidos asociados a esas entregas
    #pedidos_por_entregar = Pedido.objects.filter(id_pedido__in=entregas_asignadas.values('id_pedido'))
    
    # Si necesitas obtener todos los clientes asociados a esos pedidos
    #clientes = Cliente.objects.filter(id_cliente__in=pedidos_por_entregar.values('id_cliente')).distinct()

    return render(request, 'repartidor/perfil-repartidor.html' )