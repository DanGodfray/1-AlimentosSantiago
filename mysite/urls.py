"""
URL configuration for mysite project.

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
#este es la importacion del ejemplo visto en clases
from alumnos import views

from . import views

#se importa paginas
#from paginas import views

#urls que el usuario puede acceder
urlpatterns = [
    path('admin/', admin.site.urls),

    #estas son las rutas del home al iniciar el servidor
    path('', include('paginas.urls')),
    path('', include('catalogos.urls')),
    
    path('home/', include('paginas.urls')),
    
    #esta es la ruta de catalogos
    path('home/', include('catalogos.urls')),
    
    #engloba todas las urls de la app alumnos
    path('alumnos/', include('alumnos.urls')),
    
#se incluye el static para que se puedan ver las imagenes en el servidor    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

