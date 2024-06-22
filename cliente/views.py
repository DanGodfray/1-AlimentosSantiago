from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ecommerce.models import Categoria, Plato, Pedido
from .models import Cliente
from proveedor.models import Proveedor
from repartidor.models import Repartidor
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    context={} 
    return render(request, 'cliente/home.html')

def main(request):
    context={} 
    return render(request, 'cliente/main.html')

def perfilClientes(request, mensaje=None):
    plato = Plato.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    repartidores = Repartidor.objects.all()
    clientes = Cliente.objects.all()

    for p in plato:
        if not p.foto_plato:
            p.foto_plato = 'img/Ui-12-1024.webp'

    if mensaje is not None:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes,'mensaje': mensaje, }
        return render(request, 'cliente/perfil-cliente.html', context)
    else:
        context = {"listaPlatos": plato, "listaCategorias": categorias, "listaProveedores": proveedores, "listaRepartidores": repartidores, "listaClientes": clientes }
        return render(request, 'cliente/perfil-cliente.html', context)


