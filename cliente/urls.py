from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.homeCliente, name='homeCliente'),
    #path('main/', views.main, name='main'),
    
    path('login-cliente/', views.loginCliente, name='loginCliente'),
    path('logout/', views.logoutCliente, name='logoutCliente'), 
    path('registrarse/', views.registrarCliente, name='registrarCliente'),
    
    
    path('cliente/', views.perfilClientes, name='perfilCliente'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)