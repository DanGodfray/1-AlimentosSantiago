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

#-------------------------VIEWS DE CATALOGOS-------------------------

def listarCatalogos(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    categoria = Categoria.objects.order_by('?').first()
    plato = Plato.objects.order_by('?').first()
    oferta = Plato.objects.filter(descuento_activo=True).order_by('?').first()
    context = {"categorias": [categoria], "platos": [plato], "ofertas": [oferta]}
    return render(request, 'ecommerce/catalogos.html', context)

banderaCatActivo = False

def listarCategorias(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    banderaCatActivo = True
    categoria = Categoria.objects.filter(cat_activo=True).all()
    context = {"arregloCat":categoria, "banderaCatActivo":banderaCatActivo}
    return render(request, 'ecommerce/categorias.html', context)

banderaOferta = False

def listarOfertas(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    banderaOferta = True
    plato = Plato.objects.filter(descuento_activo=True)
    context = {"platos":plato, "banderaOferta":banderaOferta}
    return render(request, 'ecommerce/platos.html', context)

#view para probar el listado de platos sin parametros
def listarPlatos(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    plato = Plato.objects.all()
    
    context = {"platos":plato}
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
    context = {"platos":plato}
    return render(request, 'ecommerce/platos.html', context)

#-------------------------FIN VIEWS DE CATALOGOS-------------------------

#-------------------------VIEWS DE CARRO DE COMPRAS-------------------------

def avisoCarro(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    messages.success(request, f'Debe iniciar sesion para acceder al carro de compras')
    
    return redirect('homeCliente')

#view para agregar un plato al carro
@login_required
def carroEstado(request):
    if not usuarioValido(request, 'cliente'):
        return redirect('homeCliente') 
    
    return render(request, 'cart/carro.html')


#view para agregar un plato al carro
@login_required
def agregarAlCarro(request):
    #if not usuarioValido(request, 'cliente'):
    #    return redirect('homeCliente') 
    
    #se obtiene el id del plato que se desea agregar al carro
    carro = Carro(request)

    if request.POST.get('action') == 'post':
        id_plato = request.POST.get('id_plato')
        
        plato = get_object_or_404(Plato, id_plato=id_plato)
        #se agrega el plato al carro y a la sesion
        carro.add(plato=plato)
        #se guarda el carro en la sesion y se retorna una respuesta en formato json
        response=JsonResponse({'Nombre plato: ', plato.nombre_plato, 'Precio: ', plato.precio_plato})
        
        return response

    

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
