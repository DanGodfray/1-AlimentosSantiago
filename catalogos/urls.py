from django.urls import path
from . import views

urlpatterns = [
    path('catalogos/', views.catalogos , name='catalogos'),
    
]