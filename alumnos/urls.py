from django.urls import path
from . import views


urlpatterns = [
   
   path('index', views.index, name='index'),
   path('listadoSQL', views.listadoSQL, name='listadoSQL'),
   path('listaGeneros', views.listaGeneros, name='listaGeneros'),
   
   # esta es una vista que recibe un parametro usuario, que se pasa por la url de index
   path('index/<str:user>', views.indexUser, name='index'),
   
   #esta es una vista que se llama cuando se accede a la url tasks
   path('tasks/', views.tasks, name='tasks'),
   
   #esta es una vista que se llama cuando se accede a la url projects
   path('projects/', views.projects, name='projects'),
   

    
]