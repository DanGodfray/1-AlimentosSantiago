from django.db import models
import datetime

class Proveedor(models.Model):
        id_proveedor = models.AutoField(db_column='idProveedor',primary_key=True)
        nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)
        
        #credenciales de acceso
        fono_proveedor = models.DecimalField(max_digits=10,decimal_places=2,max_length=15, blank=False, null=False)
        email_proveedor = models.EmailField(max_length=100, blank=False, null=False)
        password_proveedor = models.CharField(max_length=100, blank=False, null=False)

        def __str__(self):
            return self.nombre_proveedor