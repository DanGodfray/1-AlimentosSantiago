from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


# urlpatterns = [
#     
#     #se importa la vista home
#     path('', views.home, name='home'),
#     
#     #alternativa a la vista home
#     path('main/', views.main, name='main'),
#     
#     path('proveedor/', views.perfilProveedores, name='proveedor'),
#     
#     path('proveedor/<str:prov>', views.listarPlatosPorProv, name='listarPlatosPorProv'),
#     
#     path('proveedor/registrar-plato/', views.registrarPlato , name='registrarPlato'),
#     
#     path('proveedor/eliminar-publicacion/<str:pkplato>/', views.eliminarPlato , name='eliminarPlato'),
#     
#     path('proveedor/estado-plato/<str:pk>/', views.pausarPlato, name='pausarPlato'),
#     
#     path('proveedor/editar-publicacion/<str:pkplato>', views.editarPlato , name='editarPlato'),
#     
# ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)