from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #-------------------------URLS DE CATALOGOS-------------------------
    #url que muestra el catalogo general
    path('catalogos/', views.listarCatalogos , name='catalogos'),
    
    #url que muestra
    path('catalogos/categorias/', views.listarCategorias , name='categorias'),
    
    #solo se listan los que se encuentran en oferta
    path('catalogos/platos/ofertas', views.listarOfertas , name='platos-ofertas'),
    
    path('catalogos/platos/', views.listarPlatos , name='platos'),
    
    #este path se utiliza para mostrar los platos de una categoria seleccionada
    path('catalogos/categoria/<str:cat>', views.platosCategoriaSeleccionada , name='platosCategoriaSeleccionada'),
    #-------------------------FIN URLS DE CATALOGOS-------------------------
    
    #-------------------------URLS DE CHECKOUT ALFA-------------------------
    
    ###path('checkout/', views.checkout, name='checkout'),
    ###path('thankyou/', views.thankyou, name='thankyou'),
    
    #-------------------------FIN URLS DE CHECKOUT ALFA-------------------------
    
    #-------------------------URLS DE CARRO V2-------------------------
    
    path('home/carro', views.avisoCarro, name='avisoCarro'),
    
    path('cliente/carro/', views.carroEstado, name='carroEstado'),
    path('cliente/carro/agregar', views.agregarAlCarro, name='agregarAlCarro'),
    path('cliente/carro/eliminar', views.eliminarCarro, name='eliminarCarro'),
    path('cliente/carro/editar', views.editarCarro, name='editarCarro'),
    
    
    #-------------------------FIN URLS DE CARRO V2-------------------------

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)