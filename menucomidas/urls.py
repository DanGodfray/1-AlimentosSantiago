from django.urls import path
from . import views

#aqui se definen las urls que se pueden acceder en la app menucomidas/
urlpatterns = [
    #debe indicar una vista de pagina principal
    path('index', views.index, name='index'),

]
