from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Plato
from django.core.paginator import Paginator
from django.contrib import messages


banderaOferta = False

# Create your views here.

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