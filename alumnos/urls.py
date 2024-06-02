from django.urls import path
from . import views


urlpatterns = [
   
   path('index', views.index, name='index'),
   path('listadoSQL', views.listadoSQL, name='listadoSQL'),
   path('listaGeneros', views.listaGeneros, name='listaGeneros'),
   
   # esta es una vista que recibe un parametro usuario
   path('index/<str:user>', views.index, name='index'),
    
]