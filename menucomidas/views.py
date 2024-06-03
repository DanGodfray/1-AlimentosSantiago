from django.shortcuts import render


#se debe importar el objeto al cual se le va a hacer referencia en la vista y se le almacena los datos captados en una variable, esto es para captura de datos en el url mismo
from django.http import HttpResponse, JsonResponse


# Create your views here.

#este metodo ayuda a renderizar la pagina menu.html
def index(request):
    #esto es la pagina principal de menucomidas
    return render(request, 'menucomidas/menu.html')
