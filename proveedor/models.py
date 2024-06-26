from django.db import models
import datetime
from django.contrib.auth.models import User

class Proveedor(models.Model):
        id_proveedor = models.AutoField(db_column='idProveedor',primary_key=True)
        nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)
        
        user = models.OneToOneField(User, on_delete=models.CASCADE)

        fono_proveedor = models.DecimalField(max_digits=10,decimal_places=2,max_length=15, blank=False, null=False)
        

        def save(self, *args, **kwargs):
            self.nombre_proveedor = self.id_proveedor.nombre_proveedor
            super().save(*args, **kwargs)