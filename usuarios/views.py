from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ecommerce.models import Categoria, Plato
from .models import Proveedor, Venta
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404

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
def pausarPlato(request, pk):
    plato = get_object_or_404(Plato, id_plato=pk)
    
    if request.method == 'POST':
        # Toggle the plato_activo field
        plato.plato_activo = not plato.plato_activo
        plato.save()
        # Redirect back to the page listing the publications
        return redirect('proveedor')  # Replace with the actual name of your view

    return render(request, 'usuarios/proveedor.html', {'plato': plato})

def platoEsPost(r):
    print("entro a esPost") 
    categoria = r.POST.get('categoria')
    nombre = r.POST.get('nombre')
    descripcion = r.POST.get('descripcion')
    precio = r.POST.get('precio')
    oferta = r.POST.get('oferta')
    foto = r.FILES.get('foto')
    proveedor = r.POST.get('proveedor')
    
    #se registra la fecha de registro del plato
    fecha = date.today()
    
    #se obtiene el estado del descuento
    descuento = r.POST.get('descuento_activo')
    if descuento == 'on':
        descuento = True
    else:
        descuento = False
    
    #se obtiene el estado del plato
    plato_activo = r.POST.get('plato_activo')
    if plato_activo == 'on':
        plato_activo = True
    else:
        plato_activo = False
    
    objetoProveedor = Proveedor.objects.get(nombre_proveedor=proveedor)
    
    #se obtiene el id de la categoria seleccionada
    objetoCategoria = Categoria.objects.get(nom_categoria=categoria)
    
    if foto:
        fs = FileSystemStorage()
        filename = fs.save(foto.name, foto)
        uploaded_file_url = fs.url(filename)
    else:
        uploaded_file_url = None
    
    #se crea el objeto plato
    objetoPublicacion = Plato(
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
    
    objetoPublicacion.save()
    context = {"mensaje":"Plato registrado correctamente"}
    #messages.success(request, 'Plato registrado correctamente')
    return render(r, 'usuarios/plato_add.html', context)

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
            
            print("se renderio default")
            
            return render(request, 'usuarios/plato_add.html', context)
            
        else:    
            print("es post")    
            
            platoEsPost(request)
        
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
        
def editarPlato(request, pkplato):
    
    print(f'pkplato: {pkplato}')
     
    if pkplato != "":
        
        plato = get_object_or_404(Plato, id_plato=pkplato)
        print(f'plato obj: {plato}')
        
        extraidoPlato = Plato.objects.get(id_plato=pkplato)
        print(f'extraidoPlato: {extraidoPlato}')
        
        categoria = Categoria.objects.all()
        print(f'categoria obj: {categoria}')
        
        proveedor = Proveedor.objects.all()
        print(f'proveedor obj: {proveedor}')
        #alumno=Alumno.objects.get(rut=pk)
        

        debug = {plato, categoria, proveedor}
        print(f'esto es un debug de contenido: {debug}')
        
        
        context={'listaPlatos':plato ,'listaCategorias':categoria, 'listaProveedores':proveedor}
        #context={'listaAlumnos':alumno, 'listaGeneros':obtenerListaGeneros()}
        #la lista listaAlumnos se llena con el objeto alumno y la lista listaGeneros se llena con el metodo obtenerListaGeneros(), mediante la listaAlumnos se renderea en el template alumnos_edit.html
        
        if plato:
            return render(request, 'usuarios/plato_edit.html', context)
        else:
            context ={"mensaje":"Error al editar plato"}
            return render(request, '/proveedor.html', context)
    
    if request.method == 'POST':
        platoEsPost(request)
        # Redirect back to the page listing the publications
        return redirect('proveedor')  # Replace with the actual name of your view

    return render(request, 'usuarios/proveedor.html', {'plato': plato})