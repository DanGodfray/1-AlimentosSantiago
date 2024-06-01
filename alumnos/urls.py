from django.urls import path
from . import views


urlpatterns = [
   
   path('index', views.index, name='index'),
   path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    
]