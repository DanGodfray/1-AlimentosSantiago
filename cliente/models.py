from django.db import models
from django.contrib.auth.models import User
import datetime


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    nombre_cliente = models.CharField(max_length=100, blank=False, null=False)
    apellido_cliente = models.CharField(max_length=100, blank=True, null=True)
    
    rut_cliente = models.CharField(max_length=12, blank=False, null=False)
    fono_cliente = models.DecimalField(max_digits=10,decimal_places=2,max_length=15, blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)
    direccion_cliente = models.CharField(max_length=100, blank=True, null=True)
    saldo_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=35000)
    

    #credenciales de acceso
    #email_cliente = models.EmailField(max_length=100, blank=False, null=False)
    #password_cliente = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return f'{self.nombre_cliente}{self.apellido_cliente}'
