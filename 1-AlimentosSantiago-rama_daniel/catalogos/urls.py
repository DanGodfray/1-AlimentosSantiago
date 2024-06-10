from django.urls import path
from . import views
from mysite import settings
from django.conf.urls.static import static

urlpatterns = [
    
    
    path('catalogos/', views.categorias , name='catalogos'),
    
    #no se puede recorrer 2 tablas distintas en la misma vista, se debe crear una vista para cada tabla
    #path('catalogos/pizzas', views.listaPizzas , name='platos'),
    
    path('categorias/<str:cat>', views.categoriaSeleccionada , name='categorias'),
    
    path('catalogos/platos/<int:pk>', views.platoSeleccionado, name='platos'),
        
    #el name= es importante, debe ser igual a la url para no perderse en la navegacion
    path('catalogos/platos/', views.platos , name='platos'),
    
    #------------aqui va se va insertar la version funcional de listar por categoria
    path('catalogos/platos/<str:cat>', views.platosCategoria , name='platosCategoria'),
    
    path('catalogos/platos/<str:cat>', views.categoriaSeleccionada , name='categorias'),
    
]