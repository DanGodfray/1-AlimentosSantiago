from django.urls import path
from . import views

urlpatterns = [
    path('catalogos/', views.catalogos , name='catalogos'),
    
    #el name= es importante, debe ser igual a la url para no perderse en la navegacion
    path('catalogos/platos/', views.platos , name='platos'),
]