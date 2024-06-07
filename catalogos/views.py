#se ipmporta render para renderizar las vistas
from django.shortcuts import render

#se importa redirect para redirigir urls con parametros
from django.shortcuts import redirect

#se importa messages para mostrar mensajes en pantalla
from django.contrib import messages

#se debe importar los modelos que se van a registrar
from .models import Plato, Categoria

# Create your views here.

def platos(request):
    plato = Plato.objects.all()
    context = {"platos":plato}
    return render(request, 'catalogos/platos.html', context)

def categorias(request):
    categoria = Categoria.objects.all()
    context = {"arreglo":categoria}
    return render(request, 'catalogos/catalogos.html', context)

def listarAlgo(request):
    plato = Plato.objects.raw('SELECT * FROM catalogos_categoria')
    #plato = Plato.objects.all()
    #print(plato)
    context = {"arreglo":plato}
    return render(request, 'catalogos/platos.html', context)

#methodo para seleccionar una categoria con parametro de entrada el nombre de la categoria
def categoriaSeleccionada(request, cat):
    #reemplaza guiones y guiones bajos por espacios
    cat = cat.replace("_", " "), cat.replace("-", " ")
    
    try:
        #busca la categoria seleccionada
        categoria = Categoria.objects.get(nom_categoria=cat)
        idCategoria = Categoria.objects.filter(id_categoria=categoria)
        plato = Plato.objects.filter(nom_plato=idCategoria)
        #context = {"platos":plato}
        return render(request, 'categorias.html', {'platos':plato, 'categoria':categoria})

    except:
        messages.success(request, ('No se encontra la categoria seleccionada'))
        return redirect('home')
      
      
def platoSeleccionado(request, pk):
    plato = Plato.objects.get(id=pk)
    return render(request, 'plato.html', {'plato':plato})  

