from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    #se importa la vista home
    path('', views.home, name='home'),
    
    #alternativa a la vista home
    path('main/', views.main, name='main'),
    
    
]