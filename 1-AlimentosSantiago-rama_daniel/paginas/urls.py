from django.urls import path
from . import views

urlpatterns = [
    #se importa la vista home
    path('', views.home, name='home'),
    
    #alternativa a la vista home
    path('main/', views.main, name='main'),
    
    
    
]