from django.db import models
import datetime

class Proveedor(models.Model):
        id_proveedor = models.AutoField(db_column='idProveedor',primary_key=True)
        nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)

        def __str__(self):
            return self.nombre_proveedor