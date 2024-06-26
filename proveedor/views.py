from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ecommerce.models import Categoria, Plato, Pedido, Agenda , Entrega
from .models import Proveedor
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import ProveedorRegistroForm

# Create your views here.

banderaPlatoActivo = True

def homeProveedor(request):
    proveedor=request.user
    context={'proveedor':proveedor} 
    return render(request, 'proveedor/home-proveedor.html', context)

#def mainProveedor(request):
    context={} 
    return render(request, 'proveedor/main.html')

#----------------------------------autenticacion de proveedor

def loginProveedor(request):
    if request.method == 'POST':
        username = request.POST.get('usernameProveedor')
        password = request.POST.get('passwordProveedor')
        proveedor = authenticate(request, username=username, password=password)
        
        if proveedor is not None:
            print(f'Proveedor: {proveedor} autenticado')
            login(request, proveedor)
            messages.success(request, f'Bienvenido {username}!')
            return redirect('proveedor')
        else:
            print(f'proveedor: {proveedor} no autenticado')
            messages.error(request, 'Usuario o contraseña incorrecta, vuelva a intentarlo.')
            return redirect('loginProveedor')
    else:
        return render(request, 'proveedor/login-proveedor.html',{})    
    
def registrarProveedor(request):
    if request.method == 'POST':
        form = ProveedorRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Proveedor registrado exitosamente.')
            return redirect('proveedor')
        else:
            #si ocurrio un error se elimina el usuario creado
            username = request.POST.get('username')  # Assuming 'username' is a required field
            if username:
                try:
                    user = User.objects.get(username=username)
                    user.delete()
                    messages.error(request, 'Error: no se pudo registrar el usuario.')
                except User.DoesNotExist:
                    pass  #si el usuario no esta creado
            else:
                messages.error(request, 'Error: no se pudo registrar el usuario.')
    else:
        form = ProveedorRegistroForm()
    return render(request, 'proveedor/registrarse-proveedor.html', {'form': form})
    
@login_required
def logoutProveedor(request):
    context={} 
    try:
        logout(request)
        messages.success(request, f'Se ha cerrado sesión correctamente.')
        redirect('homeProveedor')
    except Exception as e:
        messages.error(request, f'Error al cerrar sesión: {e}')
    return redirect('homeProveedor')

#----------------------------------fin autenticacion de proveedor

@login_required
def perfilProveedores(request, mensaje=None):
    
    try:
        proveedores = Proveedor.objects.get(user=request.user)
    except Proveedor.DoesNotExist:
        messages.error(request, 'El usuario de proveedor es incorrecto o no existe. intentelo denuevo o registrese como proveedor.')
        return redirect('homeProveedor') 
    
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.get(user=request.user)

    if proveedores:
        for p in plato:
            if not p.foto_plato:
                p.foto_plato = 'img/Ui-12-1024.webp'

        if mensaje is not None:
            context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores,'mensaje': mensaje, }
            return render(request, 'proveedor/perfil-proveedor.html', context)
        else:
            context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores }
            return render(request, 'proveedor/perfil-proveedor.html', context)
    else:
        messages.error(request, 'Proveedor no encontrado')
        return redirect('proveedor')

#metodo para listar todos los platos en el perfil del proveedor, y almacena un mensaje
def publicacionProveedores(request, mensaje=None):
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    for p in plato:
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'

    if mensaje is not None:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores,'mensaje': mensaje, }
        return render(request, 'proveedor/publicaciones.html', context)
    else:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores }
        return render(request, 'proveedor/publicaciones.html', context)
    

#metodo para listar los platos por proveedor en el perfil del proveedor
def listarPlatosPorProv(request, prov):
    proveedor = get_object_or_404(Proveedor, nombre_proveedor=prov.replace("-", " "))
    plato = Plato.objects.filter(id_proveedor=proveedor.id_proveedor)
    
    for p in plato:
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'
    
    context = {"listaPlatos": plato, "listarProveedor": proveedor, "banderaProv": prov}
    return render(request, 'proveedor/publicaciones.html', context)

def pausarPlato(request, pk):
    plato = get_object_or_404(Plato, id_plato=pk)
    
    if request.method == 'POST':
        plato.plato_activo = not plato.plato_activo
        plato.save()
        messages.success(request, f"Plato '{plato.nom_plato}' {'ACTIVADO' if plato.plato_activo else 'PAUSADO'} correctamente.")
        mensaje = {'mensaje':f'El plato {plato.nom_plato} ha sido {"activado" if plato.plato_activo else "pausado"} correctamente.'}
        
        return publicacionProveedores(request, mensaje)
    
    return render(request, 'proveedor/publicaciones.html', {'plato': plato})

#metodo que rellena la tabla plato con los datos ingresados por el proveedor
def platoEsPost(request, plato=None):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        oferta = request.POST.get('oferta')
        foto = request.FILES.get('foto')
        fecha = date.today()

        descuento = request.POST.get('descuento_activo') == 'on'
        plato_activo = request.POST.get('plato_activo') == 'on'

        # Get the logged-in User instance
        user = request.user
        
        # Get the Proveedor associated with the logged-in User
        proveedor = get_object_or_404(Proveedor, user=user)

        objetoCategoria = get_object_or_404(Categoria, nom_categoria=categoria)

        # Save the uploaded image
        if foto:
            fs = FileSystemStorage()
            filename = fs.save(foto.name, foto)
            uploaded_file_url = fs.url(filename)
        else:
            uploaded_file_url = None
        
        if plato is None:
            # Create new Plato
            plato = Plato(
                id_categoria=objetoCategoria,
                nom_plato=nombre,
                descripcion_plato=descripcion,
                precio_plato=precio,
                oferta_plato=oferta,
                foto_plato=foto if uploaded_file_url else None,
                fecha_publicacion=fecha,
                descuento_activo=descuento,
                plato_activo=plato_activo,
                id_proveedor=proveedor
            )
            plato.save()
            messages.success(request, "Plato registrado correctamente.")
            
            return redirect('registrarPlato')
        else:
            # Update existing Plato
            plato.id_categoria = objetoCategoria
            plato.nom_plato = nombre
            plato.descripcion_plato = descripcion
            plato.precio_plato = precio
            plato.oferta_plato = oferta
            if uploaded_file_url:
                plato.foto_plato = foto
            plato.fecha_publicacion = fecha
            plato.descuento_activo = descuento
            plato.plato_activo = plato_activo
            plato.id_proveedor = proveedor
            plato.save()
            messages.success(request, "Plato editado correctamente.")
            
            return redirect('publicaciones')

def registrarPlato(request):
    if request.method == 'POST':
        
        print('REGISTRARPLATO: ESTO ES UN POST')
        
        return platoEsPost(request)
    else:
        print('REGISTRARPLATO: ESTO NO ES UN POST')
        
        plato = Plato.objects.all()
        categorias = Categoria.objects.all()
        proveedores = Proveedor.objects.all()
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores}
        return render(request, 'proveedor/plato_add.html', context)

def eliminarPlato(request, pkplato):
    try:
        plato = get_object_or_404(Plato, id_plato=pkplato)
        plato.delete()
        messages.success(request, 'Plato eliminado correctamente')
    except Exception as e:
        messages.error(request, f"Error al eliminar el plato: {e}")
    return redirect('publicaciones')

def editarPlato(request, pkplato):
    plato = get_object_or_404(Plato, id_plato=pkplato)
    if request.method == 'POST':
        return platoEsPost(request, plato)
    else:
        categorias = Categoria.objects.all()
        proveedores = Proveedor.objects.all()
        context = {'listaPlatos': plato, 'listaCategorias': categorias, 'listaProveedores': proveedores}
        return render(request, 'proveedor/plato_edit.html', context)