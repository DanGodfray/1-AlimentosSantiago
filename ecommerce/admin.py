from django.contrib import admin

#se debe importar los modelos que se van a registrar
from .models import  Plato, Categoria, Entrega, Pedido, Agenda

# Register your models here.

admin.site.register(Plato)
admin.site.register(Categoria)
admin.site.register(Entrega)
admin.site.register(Pedido)
admin.site.register(Agenda)