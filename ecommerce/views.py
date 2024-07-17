from django.db import IntegrityError
from django.forms import DecimalField
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Categoria, Plato
from django.core.paginator import Paginator
from django.contrib import messages
from proveedor.models import Proveedor
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group, AnonymousUser
from django.contrib.auth.decorators import login_required
from .carro import Carro
from .models import Pedido, Agenda, Entrega, itemPedido
import json


def checkout(request):
    return render(request, 'ecommerce/checkout.html')

def thankyou(request):
    return render(request, 'ecommerce/thankyou.html')


# Create your views here.

#--------funcion que se reutiliza para validar el usuario que accede a las vistas
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

#--------funcion que se reutiliza para visualizar la cantidad de items en el carro de compras
def visualizarCantidadCarro(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(id_cliente=cliente, completado=False)
        items = pedido.itempedido_set.all()
        itemsCarro = pedido.get_cantidad_items_pedido
    else:
        items = []
        pedido = {'get_total_item_oferta_descontada':0, 'get_total_item':0, 'get_cantidad_items_pedido':0}
        itemsCarro = pedido['get_cantidad_items_pedido']
        
    return itemsCarro

#-------------------------VIEWS DE CATALOGOS-------------------------

def listarCatalogos(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    categoria = Categoria.objects.order_by('?').first()
    plato = Plato.objects.order_by('?').first()
    oferta = Plato.objects.filter(descuento_activo=True).order_by('?').first()
    context = {"categorias": [categoria], "platos": [plato], "ofertas": [oferta], "itemsCarro": visualizarCantidadCarro(request)}
    return render(request, 'ecommerce/catalogos.html', context)

banderaCatActivo = False

def listarCategorias(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    banderaCatActivo = True
    categoria = Categoria.objects.filter(cat_activo=True).all()
    context = {"arregloCat":categoria, "banderaCatActivo":banderaCatActivo, "itemsCarro": visualizarCantidadCarro(request)}
    return render(request, 'ecommerce/categorias.html', context)

banderaOferta = False

banderaOferta = False

def listarOfertas(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    banderaOferta = True
    plato = Plato.objects.filter(descuento_activo=True)
    context = {"platos":plato, "banderaOferta":banderaOferta, "itemsCarro": visualizarCantidadCarro(request)}
    return render(request, 'ecommerce/platos.html', context)

#view para probar el listado de platos sin parametros
#view para probar el listado de platos sin parametros
def listarPlatos(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    plato = Plato.objects.all()
    
    
    context = {"platos":plato, "itemsCarro": visualizarCantidadCarro(request)}
    #debug para revisar el nombre de los proveedores en el objeto plato
    for plato in context['platos']:
        print(f'nombre proveedor: {plato.id_proveedor.nombre_proveedor}')
    
    #debug para revisar el nombre de los proveedores en el objeto plato
    for plato in context['platos']:
        print(f'nombre proveedor: {plato.id_proveedor.nombre_proveedor}')
    
    return render(request, 'ecommerce/platos.html', context)
    
def platosCategoriaSeleccionada(request,cat):  
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    #nombre de la categoria como parametro de entrada
    categoria = Categoria.objects.get(nom_categoria=cat)
    #selecciona los platos que pertenecen a la categoria seleccionada
    categoria = categoria.id_categoria
    #platos de la categoria seleccionada comparandola con el id de la categoria
    plato = Plato.objects.filter(id_categoria=categoria)
    nomCategoria = cat
    context = {"platos":plato, "nomCategoria":nomCategoria, "itemsCarro": visualizarCantidadCarro(request)}
    return render(request, 'ecommerce/platos.html', context)

#-------------------------FIN VIEWS DE CATALOGOS----------------------<<<<
@login_required
def actualizarCarro(request):
    data= json.loads(request.body)
    platoId = data['platoId'] #actualiza los datos del js
    action = data['action'] #actualiza los datos del js
    
    print(f'ID_PLATO: {platoId}, ACTION: {action}')
    
    cliente = request.user.cliente
    plato = Plato.objects.get(id_plato=platoId)
    pedido, created = Pedido.objects.get_or_create(id_cliente=cliente, completado=False)    
    
    pedidoItemVar, created = itemPedido.objects.get_or_create(pedido=pedido, plato=plato)
    
    if action == 'agregar':
        pedidoItemVar.cantidad_item = (pedidoItemVar.cantidad_item + 1)
    elif action == 'quitar':
        pedidoItemVar.cantidad_item = (pedidoItemVar.cantidad_item - 1)
    
    if pedidoItemVar.cantidad_item <= 0 or action == 'eliminar':
        pedidoItemVar.delete()   
    
    print(f'Cantidad antes de guardar: {pedidoItemVar.cantidad_item},')
    
    try:
        pedidoItemVar.save()
        print(f'Se guardó exitosamente: {pedidoItemVar}')
    except IntegrityError as e:
        print(f'Error al guardar: {e}')
    
    return JsonResponse('Carro actualizado', safe=False)

#-------------------------VIEWS DE CARRO DE COMPRAS----------------------<<<<

def avisoCarro(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    messages.success(request, f'Debe iniciar sesion para acceder al carro de compras')
    
    return redirect('homeCliente')


#view para agregar un plato al carro
#@login_required
def carroEstado(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    if request.user.is_authenticated:
        cliente = request.user.cliente
        
        #se crea un pedido si no existe uno
        pedido, created = Pedido.objects.get_or_create(id_cliente=cliente, completado=False)
        items = pedido.itempedido_set.all()
        
    else:
        items = []
        pedido = {'get_total_item_oferta_descontada':0, 'get_total_item':0, 'get_cantidad_items_pedido':0}
   
        
    context = {'listaItems':items, 'listaPedidos':pedido , 'itemsCarro': visualizarCantidadCarro(request)}
    
    print(f'PEDIDO: {pedido}, estado almacenado: {pedido.completado}, cliente: {cliente}')
    
    return render(request, 'cart/carro.html', context)

#view para verificar el carro de compras del cliente
@login_required
def verificarCarro(request):
    
    if request.user.is_authenticated:
        cliente = request.user.cliente
        
        #se crea un pedido si no existe uno
        pedido, created = Pedido.objects.get_or_create(id_cliente=cliente, completado=False)
        items = pedido.itempedido_set.all()
        
    else:
        items = []
        pedido = {'get_total_item_oferta_descontada':0, 'get_total_item':0, 'get_cantidad_items_pedido':0}
   
        
    context = {'listaItems':items, 'listaPedidos':pedido, 'itemsCarro': visualizarCantidadCarro(request)}
    
    print(f'VERIFICAR CARRO: {pedido}, estado almacenado: {pedido.completado}, cliente: {cliente}')
    
    return render(request, 'cart/verficar-carro.html', context)

#view para agregar un plato al carro
@login_required
def agregarAlCarro(request):
    carro = Carro(request)

    if request.POST.get('action') == 'post':
        id_plato = request.POST.get('id_plato')
        
        if not id_plato:
            return JsonResponse({'error': 'No se ha seleccionado un plato'}, status=400)

        try:
            id_plato = int(id_plato)
        except ValueError:
            return JsonResponse({'error': 'ID de plato no válido'}, status=400)

        plato = get_object_or_404(Plato, id_plato=id_plato)
        carro.add(plato=plato)

        print(f'ID_PLATO que se agrego es: {id_plato}')
        print(f'ID_PLATO 2da vez: {id_plato}')
        print(f'Plato: {plato.nom_plato}')
        print(f'Carro: {carro.carro.get(str(id_plato))}')

        response = JsonResponse({
            'Nombre plato': plato.nom_plato,
            'Precio': plato.oferta_plato if plato.descuento_activo else plato.precio_plato
        })
        
        return response
    
    return JsonResponse({'error': 'No se ha seleccionado un plato'}, status=400)

#view para eliminar la cantidad en el carro
@login_required
def eliminarCarro(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    '''
    #se obtiene el id del plato que se desea eliminar del carro
    idPlato = request.GET.get('id')
    #se obtiene el id del cliente que esta realizando la compra
    idCliente = request.user.id
    
    #se obtiene el plato que se desea eliminar del carro
    plato = Plato.objects.get(id_plato=idPlato)
    #se obtiene el cliente que esta realizando la compra
    cliente = User.objects.get(id=idCliente)
    
    #se obtiene el carro de compras
    carro = Carro.objects.get(id_cliente=cliente)
    #se obtiene el detalle del carro de compras
    detalleCarro = DetalleCarro.objects.get(id_plato=plato, id_carro=carro)
    
    #se elimina el detalle del carro de compras
    detalleCarro.delete()
    '''
    
    #context = {"carro":carro, "detallesCarro":detallesCarro}
    
    #return render(request, 'cart/carro.html', context)
    pass

@login_required
def editarCarro(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    '''
    #se obtiene el id del plato que se desea editar del carro
    idPlato = request.GET.get('id')
    #se obtiene la cantidad de platos que se desea agregar al carro
    cantidad = request.GET.get('cantidad')
    #se obtiene el id del cliente que esta realizando la compra
    idCliente = request.user.id
    
    #se obtiene el plato que se desea agregar al carro
    plato = Plato.objects.get(id_plato=idPlato)
    #se obtiene el cliente que esta realizando la compra
    cliente = User.objects.get(id=idCliente)
    
    #se obtiene el carro de compras
    carro = Carro.objects.get(id_cliente=cliente)
    #se obtiene el detalle del carro de compras
    detalleCarro = DetalleCarro.objects.get(id_plato=plato, id_carro=carro)
    
    #se actualiza la cantidad de platos en el detalle del carro de compras
    detalleCarro.cantidad = cantidad
    detalleCarro.save()
    
    #se obtienen los detalles del carro de compras
    detallesCarro = DetalleCarro.objects.filter(id_carro=carro)
    '''
    
    #context = {"carro":carro, "detallesCarro":detallesCarro}
    
    #return render(request, 'cart/carro.html', context)
    pass
