from django.db import models
#from ecommerce.models import Plato, Categoria
import datetime



# Create your models here.

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)
    
   #ventas = models.ForeignKey('Venta', on_delete=models.CASCADE, db_column='ventas_id_venta')

    def __str__(self):
        return self.nombre_proveedor
     
    
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    monto_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    fecha_venta = models.DateField(blank=False, null=False)

    #id_proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, db_column='idProveedor',default=1)

    def __str__(self):
        return f"Venta {self.id_venta}"