from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#se crea una vista para el home
def home(request):
    return render(request, 'paginas/home.html')

def main(request):
    return render(request, 'paginas/main.html')