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
# Create your views here.

banderaPlatoActivo = True

def homeProveedor(request):
    context={} 
    return render(request, 'proveedor/home.html')

def mainProveedor(request):
    context={} 
    return render(request, 'proveedor/main.html')

def loginProveedor(request):
    context={} 
    if request.method == 'POST':
        username = request.POST.get('usernameCliente')
        password = request.POST.get('passwordCliente')
        proveedor = authenticate(request, username=username, password=password)
        if proveedor is not None:
            print(f'Proveedor: {proveedor} autenticado')
            login(request, proveedor)
            messages.success(request, f'Bienvenido {username}!')
            return redirect('home')
        else:
            print(f'cliente: {proveedor} no autenticado')
            messages.error(request, 'Usuario o contraseña incorrecta, vuelva a intentarlo.')
            return redirect('loginProveedor')
    else:
        return render(request, 'proveedor/login-proveedor.html',{})

@login_required
def perfilProveedores(request, mensaje=None):
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    for p in plato:
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'

    if mensaje is not None:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores,'mensaje': mensaje, }
        return render(request, 'proveedor/perfil-proveedor.html', context)
    else:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores }
        return render(request, 'proveedor/perfil-proveedor.html', context)

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
        messages.success(request, f"Plato {'activado' if plato.plato_activo else 'pausado'} correctamente.")
        mensaje = {'mensaje':f'El plato {plato.nom_plato} ha sido {"activado" if plato.plato_activo else "pausado"} correctamente.'}
        
        return publicacionProveedores(request, mensaje)
    
    return render(request, 'proveedor/publicaciones.html', {'plato': plato})

#metodo que rellena la tabla plato con los datos ingresados por el proveedor
def platoEsPost(request, plato=None):
    categoria = request.POST.get('categoria')
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    precio = request.POST.get('precio')
    oferta = request.POST.get('oferta')
    foto = request.FILES.get('foto')
    proveedor = request.POST.get('proveedor')
    fecha = date.today()

    descuento = request.POST.get('descuento_activo') == 'on'
    plato_activo = request.POST.get('plato_activo') == 'on'

    objetoProveedor = get_object_or_404(Proveedor, nombre_proveedor=proveedor)
    objetoCategoria = get_object_or_404(Categoria, nom_categoria=categoria)
    
    #muestra la imagen ya subida por el proveedor
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
            id_proveedor=objetoProveedor
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
        plato.id_proveedor = objetoProveedor
        plato.save()
        messages.success(request, "Plato editado correctamente.")
        mensaje = {'mensaje': 'Plato editado correctamente.'}
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