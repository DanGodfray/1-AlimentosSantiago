from django.db import models
import datetime

# Create your models here.

# Creación de la tabla Repartidor
class Repartidor(models.Model):
    id_repartidor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12, blank=False, null=False)
    nombre_repartidor = models.CharField(max_length=100, blank=False, null=False)
    numero_telf = models.CharField(max_length=15, blank=False, null=False)
    def __str__(self):
        return self.nombre_repartidor