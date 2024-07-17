from django.db import models
import datetime
from django.contrib.auth.models import User

class Proveedor(models.Model):
        id_proveedor = models.AutoField(db_column='idProveedor',primary_key=True)
        nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)
        
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        
        domicilio_proveedor = models.CharField(default='s/n', max_length=100, blank=False, null=False)

        fono_proveedor = models.IntegerField( blank=False, null=False)
        
        def __str__(self):
            return f'{self.nombre_proveedor}'

        #def save(self, *args, **kwargs):
            #self.nombre_proveedor = self.id_proveedor.nombre_proveedor
            #super().save(*args, **kwargs)