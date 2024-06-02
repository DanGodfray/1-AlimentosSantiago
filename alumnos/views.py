from django.shortcuts import render
from .models import Genero, Alumno

from django.http import HttpResponse

# Create your views here.

def index(request):
    alumnos = Alumno.objects.all()
    context ={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context ={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def listaGeneros(request):
    generos = Genero.objects.all()
    context ={"generos":generos}
    return render(request, 'alumnos/listaGeneros.html', context)

# esta es una vista que recibe un parametro usuario e imprime el nombre del usuario
def index(request, user):
    return HttpResponse("Hola " + user)