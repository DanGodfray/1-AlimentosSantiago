from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Plato
from django.core.paginator import Paginator
from django.contrib import messages


banderaOferta = False

# Create your views here.

#-------------------------VIEWS DE CATALOGOS-------------------------

def listarCatalogos(request):
    categoria = Categoria.objects.all()
    plato = Plato.objects.all()
    oferta = Plato.objects.filter(descuento_activo=True)
    context = {"categorias":categoria, "platos":plato, "ofertas":oferta}
    return render(request, 'ecommerce/catalogos.html', context)

def listarCategorias(request):
    categoria = Categoria.objects.all()
    context = {"arregloCat":categoria}
    return render(request, 'ecommerce/categorias.html', context)

def listarOfertas(request):
    banderaOferta = True
    plato = Plato.objects.filter(descuento_activo=True)
    context = {"platos":plato, "banderaOferta":banderaOferta}
    return render(request, 'ecommerce/platos.html', context)

def listarPlatos(request):
    plato = Plato.objects.all()
    context = {"platos":plato}
    return render(request, 'ecommerce/platos.html', context)
    
def platosCategoriaSeleccionada(request,cat):  
    #nombre de la categoria como parametro de entrada
    categoria = Categoria.objects.get(nom_categoria=cat)
    #selecciona los platos que pertenecen a la categoria seleccionada
    categoria = categoria.id_categoria
    #platos de la categoria seleccionada comparandola con el id de la categoria
    plato = Plato.objects.filter(id_categoria=categoria)
    
    context = {"platos":plato}
    return render(request, 'ecommerce/platos.html', context)

#-------------------------FIN VIEWS DE CATALOGOS-------------------------

def registrarPlato(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        oferta = request.POST.get('oferta')
        categoria = request.POST.get('categoria')
        foto = request.FILES.get('foto')
        
        #se obtiene el id de la categoria seleccionada
        categoria = Categoria.objects.get(nom_categoria=categoria)
        #se crea un nuevo plato
        plato = Plato(id_categoria=categoria, 
                      nom_plato=nombre, 
                      descripcion_plato=descripcion, 
                      precio_plato=precio, 
                      oferta_plato=oferta, 
                      foto_plato=foto)
        plato.save()
        messages.success(request, 'Plato registrado correctamente')
        return redirect('registroPlato')
    else:
        categoria = Categoria.objects.all()
        context = {"categorias":categoria}
        return render(request, 'ecommerce/publicaciones.html', context)