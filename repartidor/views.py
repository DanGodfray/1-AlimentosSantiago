from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ecommerce.models import Categoria, Plato, Pedido
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

def registrarCliente(request):
    if not usuarioValido(request, 'repartidor'):
        return redirect('homeRepartidor')

    if request.method == 'POST':
        form = RepartidorRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            proveedor_group = Group.objects.get(name='repartidor') #se le asigna un grupo al momento de registrarse
            user.groups.add(proveedor_group)
            login(request, user)
            messages.success(request, 'Usuario registrados exitosamente.')
            return redirect('perfilCliente')  #se redirige a la pagina de perfil de cliente
        else:
            messages.error(request, 'Error: no se pudo registrar el usuario.')
    else:
        form = RepartidorRegistroForm()

    return render(request, 'repartidor/registrarse-repartidor.html', {'form': form})