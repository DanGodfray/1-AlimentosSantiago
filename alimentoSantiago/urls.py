"""
URL configuration for alimentoSantiago project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls')),
    #path('', include('usuarios.urls')),
    path('', include('ecommerce.urls')),
    path('', include('proveedor.urls')),
    path('', include('repartidor.urls')),
    path('home/', include('cliente.urls')),
    #path('home/', include('usuarios.urls')),
    path('home/', include('ecommerce.urls')),
    path('home/', include('proveedor.urls')),
    path('home/', include('repartidor.urls')),
    
    #path('usuarios/', include('usuarios.urls')),
    #path('ecommerce/', include('ecommerce.urls')),
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
