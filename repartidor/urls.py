from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path('repartidor/',views.homeRepartidor,name='homeRepartidor'),
    path('repartidor/login/',views.loginRepartidor,name='loginRepartidor'),
    path('repartidor/logout/',views.logoutRepartidor,name='logoutRepartidor'),
    path('repartidor/registrarse/',views.registrarRepartidor,name='registrarRepartidor'),
    path('repartidor/perfil/',views.perfilRepartidor,name='perfilRepartidor'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)