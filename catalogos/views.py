from django.shortcuts import render

#se debe importar los modelos que se van a registrar
from .models import Plato, Categoria

# Create your views here.

def catalogos(request):
    platos = Plato.objects.all()
    context = {"platos":platos}
    return render(request, 'catalogos/catalogo.html', context)