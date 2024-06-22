from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    
    path('cliente/', views.perfilClientes, name='cliente'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)