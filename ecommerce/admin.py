from django.contrib import admin

#se debe importar los modelos que se van a registrar
from .models import Plato, Categoria

# Register your models here.

admin.site.register(Plato)
admin.site.register(Categoria)