from django.urls import path
from . import views


urlpatterns = [
   
   #-----------------CRUD-------------------
   
   path('index', views.index, name='index'),
   path('listadoSQL', views.listadoSQL, name='listadoSQL'),
   path('listaGeneros', views.listaGeneros, name='listaGeneros'),
   
   path('crud', views.crud, name='crud'),
   
   path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
   path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
   path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
   path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
   
   #-----------------CRUD-------------------
   
   # esta es una vista que recibe un parametro usuario, que se pasa por la url de index
   path('index/<str:user>', views.indexUser, name='index'),
   
   #esta es una vista que se llama cuando se accede a la url tasks
   path('tasks/', views.tasks, name='tasks'),
   
   #esta es una vista que se llama cuando se accede a la url projects
   path('projects/', views.projects, name='projects'),
   
   #es importante importar o referenciar el nombre de la vista en el el url correspondiente
   path('tasks/<int:id>', views.tasks, name='projects'),
   
   path('tasks2/<str:nombre>', views.tasks2, name='projects'),
   

    
]