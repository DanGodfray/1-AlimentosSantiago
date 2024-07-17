from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

# Creación de la tabla Repartidor
class Repartidor(models.Model):
    id_repartidor = models.AutoField(primary_key=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    rut_repartidor = models.CharField(max_length=12, blank=False, null=False)
    fono_repartidor = models.CharField(max_length=15, blank=False, null=False)
    def __str__(self):
        return self.rut_repartidor