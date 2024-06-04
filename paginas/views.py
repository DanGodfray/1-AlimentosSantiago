from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#se crea una vista para el index
def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de la app paginas.")
