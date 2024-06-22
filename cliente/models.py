from django.db import models
import datetime


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100, blank=False, null=False)
    rut_cliente = models.CharField(max_length=12, blank=False, null=False)
    saldo_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)

    #credenciales de acceso
    apellido_cliente = models.CharField(max_length=100, blank=True, null=True)
    fono_cliente = models.DecimalField(max_digits=10,decimal_places=2,max_length=15, blank=False, null=False)
    email_cliente = models.EmailField(max_length=100, blank=False, null=False)
    password_cliente = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return f'{self.nombre_cliente}{self.apellido_cliente}'
