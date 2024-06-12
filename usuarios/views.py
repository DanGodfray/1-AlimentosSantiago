from django.shortcuts import render

# Create your views here.

def home(request):
    context={} 
    return render(request, 'usuarios/home.html')

def main(request):
    context={} 
    return render(request, 'usuarios/main.html')