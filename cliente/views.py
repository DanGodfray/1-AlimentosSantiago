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
    
    usuarioValido(request, cliente)
    
    print(f'usuario despues de usuarioValido: {cliente}')
    plato = Plato.objects.order_by('?').all()
    
    context = {'listaPlatos': plato, 'cliente': cliente} 
    return render(request, 'cliente/home.html', context)

def main(request):
    context={} 
    return render(request, 'cliente/main.html')

def usuarioValido(request, user):
    user = request.user
    print(f'USUARIOVALIDO: user el usuario actual es: {user}')
    
    #-------------------------------------------------------puro debug
    proveedor_group = Group.objects.all()
    print(f'proveedor_group: {proveedor_group}')
    
    proveedor_group = get_object_or_404(Group, name='cliente')
    print(f'proveedor_group get_object_or_404: {proveedor_group}')
    
    userFilter = user.groups.filter(name='cliente').exists()
    print(f'user groups filter: {userFilter}')
    
    #user = request.user.groups.get().name
    try:
        group_name = request.user.groups.get().name
        print(f'user request.user.groups = group_name: {group_name}')
        group_name = request.user.groups.get().name
    except Group.DoesNotExist:
        print(f'no se pudo obtener el grupo del usuario: {user}')
        
    #-----la condicion que le hace logout al usuario que no corresponda al perfil
        
    if user.is_authenticated:
        if userFilter == True:
            print(f'usuario autenticado: {user}')
            pass #deja pasar al usuario cliente ya que es valido
        else:
            logout(request)
            messages.error(request, 'Usuario invalido.')
            return redirect('homeCliente')    
    else:
        logout(request)
        return redirect('homeCliente')
        
#----------------------------------autenticacion de cliente

def loginCliente(request):
    context={}
    user=request.user
    print(f'user en perfil: {user}')
    usuarioValido(request, user)
     
    if request.method == 'POST':
        username = request.POST.get('usernameCliente')
        password = request.POST.get('passwordCliente')
        #role = request.POST.get('role')
        user = authenticate(request, username=username, password=password)
        #equest.session['role'] = role
        
        if user is not None and usuarioValido(request, user) : 
            
            login(request, user)
            if user.groups.filter(name='cliente').exists():
                print(f'cliente: {user} autenticado')
                messages.success(request, f'Bienvenido {user}!')
            return redirect('perfilCliente')
                 
        else:
            print(f'cliente: {user} no autenticado')
            messages.error(request, 'Contraseña o usuario incorrecta, intententelo mas tarde.')
            return redirect('homeCliente')
            
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

def registrarCliente(request):
    user=request.user
    print(f'user en perfil: {user}')
    usuarioValido(request, user)
    
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  #guarda el formulario sin guardar en la base de datos
            user.save()  # se guarda el usuario
            cliente_group = Group.objects.get(name='cliente')  # get del grupo 'cliente'
            user.groups.add(cliente_group)  # se agrega el usuario al grupo 'cliente'
            messages.success(request, 'Usuario registrado exitosamente.')
            login(request, user)  # se logea el usuario
            return redirect('perfilCliente')
        else:
            username = request.POST.get('username') 
            
            if username:
                try:
                    user = User.objects.get(username=username)
                    user.delete()
                    messages.error(request, 'Error: no se pudo registrar el usuario.')
                except User.DoesNotExist:
                    pass
            else:
                messages.error(request, 'Error: no se pudo registrar el usuario.')
    else:
        form = ClienteRegistroForm()

    return render(request, 'cliente/registrarse-cliente.html', {'form': form})
    
#-------------------------------fin de autenticacion de cliente

@login_required
def perfilClientes(request, mensaje=None):
    user=request.user
    print(f'user en perfil: {user}')
    usuarioValido(request, user)
    
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    repartidores = Repartidor.objects.all()
    clientes = Cliente.objects.all()
    
    if user is None:
        messages.error(request, 'Usuario invalido.')
        return redirect('homeCliente')
    else:
        usuarioValido(request, user)
 
        for p in plato:
            if not p.foto_plato:
                p.foto_plato = 'img/Ui-12-1024.webp'

        if mensaje is not None:
            context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes,'mensaje': mensaje, 'userCliente': user}
            return render(request, 'cliente/perfil-cliente.html', context)
        else:
            context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes, 'userCliente': user}
            return render(request, 'cliente/perfil-cliente.html', context)


    #------aqui deberia comenzar if post para editar perfil de cliente