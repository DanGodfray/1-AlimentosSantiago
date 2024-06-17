from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ecommerce.models import Categoria, Plato
from .models import Proveedor, Venta
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date

# Create your views here.

banderaPlatoActivo = True

def home(request):
    context={} 
    return render(request, 'usuarios/home.html')

def main(request):
    context={} 
    return render(request, 'usuarios/main.html')

def perfilProveedores(request):
    
    plato = Plato.objects.all()
    categoria = Categoria.objects.all()
    proveedor = Proveedor.objects.all()
    
    for p in plato:
        print(f'p.foto_plato: {p.foto_plato}')
        print(f'p: {p}')
        
        #si no se ha seleccionado una foto se asigna una por defecto
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'
            
    
    context = {"listaPlatos":plato, "listaCategorias":categoria, "listaProveedores":proveedor}
    return render(request, 'usuarios/proveedor.html', context)


def listarPlatosPorProv(request,prov):  
    replace = prov.replace("-"," ") #se reemplaza el guion por un espacio 
    
    #nombre de la categoria como parametro de entrada
    proveedor = Proveedor.objects.get(nombre_proveedor=prov)
    proveedor = proveedor.id_proveedor
    
    #provedor -> plato -> categoria
    banderaProv = prov
    #platos de la categoria seleccionada comparandola con el id de la categoria
    plato = Plato.objects.filter(id_proveedor=proveedor)
    
    #si proveedor = true -> plato = true -> categoria = true
    context = {"listaPlatos":plato, "listarProveedor":proveedor, "banderaProv":banderaProv}
    return render(request, 'usuarios/proveedor.html', context)


#metodo incompleto
def pausarPlato(request):
    banderaPlatoActivo = True
    plato = Plato.objects.all()
    
    plato = plato.filter(plato_activo=False)
    
    if plato is None:
        banderaPlatoActivo = False
    
    context = {"platos":plato, "banderaPlatoActivo":banderaPlatoActivo}
    #debug para revisar el estado de los platos
    for plato in context['platos']:
        print(f'estado plato: {plato.plato_activo}')
    
    #context = {"listaPlatos": plato, "banderaPlatoActivo": banderaPlatoActivo}
    return render(request, 'usuarios/proveedor.html', context)

def registrarPlato(request):
    print("entro a registrar plato antes del try")
    try:
        print("entro al try de registrar")
        
        if request.method != 'POST':
            
            print("entro al if no es post")
            
            plato = Plato.objects.all()
            categoria = Categoria.objects.all()
            proveedor = Proveedor.objects.all()
 
            #se obtienen los datos del formulario si selecciona otra categoria   
            context = {"listaPlatos": plato ,"listaCategorias":categoria, "listaProveedores":proveedor}
            
            print("se rednderio default")
            
            return render(request, 'usuarios/plato_add.html', context)
            
        else:    
            print("es post")    
                 
            categoria = request.POST.get('categoria')
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            precio = request.POST.get('precio')
            oferta = request.POST.get('oferta')
            foto = request.FILES.get('foto')
            proveedor = request.POST.get('proveedor')
            #se registra la fecha de registro del plato
            fecha = date.today()
            #se obtiene el estado del descuento
            descuento = request.POST.get('descuento_activo')
            if descuento == 'on':
                descuento = True
            else:
                descuento = False
            #se obtiene el estado del plato
            plato_activo = request.POST.get('plato_activo')
            if plato_activo == 'on':
                plato_activo = True
            else:
                plato_activo = False
            
            objetoProveedor = Proveedor.objects.get(nombre_proveedor=proveedor)
            
            #se obtiene el id de la categoria seleccionada
            objetoCategoria = Categoria.objects.get(nom_categoria=categoria)
            
            #se crea un nuevo plato
            objetoPublicacion = Plato(id_categoria=objetoCategoria, 
                        nom_plato=nombre, 
                        descripcion_plato=descripcion, 
                        precio_plato=precio, 
                        oferta_plato=oferta, 
                        foto_plato=foto,
                        fecha_publicacion=fecha,
                        descuento_activo=descuento,
                        plato_activo=plato_activo,
                        id_proveedor=objetoProveedor)
            
            objetoPublicacion.save()
            context = {"mensaje":"Plato registrado correctamente"}
            #messages.success(request, 'Plato registrado correctamente')
            return render(request, 'usuarios/plato_add.html', context)
        
    except Exception as e:
        print(e)
        
        plato = Plato.objects.all()
        categoria = Categoria.objects.all()
        proveedor = Proveedor.objects.all()
        
        context = {"mensaje":"Error al registrar el plato", "listaPlatos": plato ,"listaCategorias":categoria, "listaProveedores":proveedor}
        messages.error(request, 'Error al registrar el plato')
        return render(request, 'usuarios/plato_add.html', context)
        
    
def eliminarPlato(request, pkplato):
    context={}
    try:
        plato = Plato.objects.get(id_plato=pkplato)
        plato.delete()
        
        print(f'plato eliminado: {plato}')
        
        plato = Plato.objects.all()
        categoria = Categoria.objects.all()
        proveedor = Proveedor.objects.all()
        context = {"mensaje":"Plato eliminado correctamente", "listaPlatos":plato, "listaCategorias":categoria, "listaProveedores":proveedor}
        messages.success(request, 'Plato eliminado correctamente')
        redirect('proveedor', context)
        return render(request, 'usuarios/proveedor.html', context)
        
        
        
    except Exception as e:
        print(e)
        plato = Plato.objects.all()
        categoria = Categoria.objects.all()
        proveedor = Proveedor.objects.all()
        context = {"listaPlatos":plato, "listaCategorias":categoria, "listaProveedores":proveedor}
        messages.error(request, 'Error al eliminar el plato')
        redirect('proveedor')
        return render(request, 'usuarios/proveedor.html', context)
        redirect('proveedor')