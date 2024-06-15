from django.db import models
import datetime
from usuarios.models import Proveedor

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria' ,primary_key=True)
    nom_categoria = models.CharField(max_length=100, blank=False, null=False)
    des_categoria = models.CharField(max_length=100, blank=True, null=True)
    foto_categoria = models.ImageField(upload_to='img/categoria', blank=True, null=True)
    cat_activo = models.BooleanField(default=True)
    
    #agrega el nombre de la categoria en el admin de django
    def _str_(self):
        return str(self.nom_categoria)

class Plato(models.Model):
    id_plato = models.AutoField(primary_key=True, blank=False, null=False)
    #se referencia id_categoria de la tabla categoria como fk para seleccionar categoria al momento de poblar la tabla plato
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria',default=1)
    nom_plato = models.CharField(max_length=100, blank=False, null=False)
    descripcion_plato = models.CharField(max_length=200, blank=True, null=True)
    precio_plato = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    oferta_plato = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    foto_plato = models.ImageField(upload_to='img/plato', blank=True, null=True)
    
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='idProveedor', default=1)
    
    fecha_publicacion = models.DateField(default=datetime.date.today)
    #banderas de actividad
    descuento_activo = models.BooleanField(default=True)
    plato_activo = models.BooleanField(default=True)

    def _str_(self):
        return self.nom_plato