from django.db import models
import datetime


class Proveedor(models.Model):
        id_proveedor = models.AutoField(db_column='idProveedor',primary_key=True)
        nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)

        def __str__(self):
            return self.nombre_proveedor

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100, blank=False, null=False)
    rut_cliente = models.CharField(max_length=12, blank=False, null=False)
    saldo_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre_cliente

# Creación de la tabla Repartidor
class Repartidor(models.Model):
    id_repartidor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12, blank=False, null=False)
    nombre_repartidor = models.CharField(max_length=100, blank=False, null=False)
    numero_telf = models.CharField(max_length=15, blank=False, null=False)
    def __str__(self):
        return self.nombre_repartidor