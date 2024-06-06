from django.urls import path
from . import views

urlpatterns = [
    
    
    path('catalogos/', views.categorias , name='catalogos'),
    
    #no se puede recorrer 2 tablas distintas en la misma vista, se debe crear una vista para cada tabla
    #path('catalogos/pizzas', views.listaPizzas , name='platos'),
    
    
    path('categorias/<str:cat>', views.categoriaSeleccionada , name='categorias'),
        
    #el name= es importante, debe ser igual a la url para no perderse en la navegacion
    path('catalogos/platos/', views.platos , name='platos'),
]