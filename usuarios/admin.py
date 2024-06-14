from django.contrib import admin

#se debe importar los modelos que se van a registrar
from .models import Proveedor, Venta

# Register your models here.

admin.site.register(Proveedor)  
admin.site.register(Venta)