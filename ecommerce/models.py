from django.db import models
import datetime

from proveedor.models import Proveedor
from repartidor.models import Repartidor
from cliente.models import Cliente


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria' ,primary_key=True)
    nom_categoria = models.CharField(max_length=100, blank=False, null=False)
    des_categoria = models.CharField(max_length=100, blank=True, null=True)
    foto_categoria = models.ImageField(upload_to='img/categoria', blank=True, null=True)
    cat_activo = models.BooleanField(default=True)

    #agrega el nombre de la categoria en el admin de django
    def _str_(self):
        return str(self.nom_categoria)

class Plato(models.Model):
    id_plato = models.AutoField(primary_key=True, blank=False, null=False)
    #se referencia id_categoria de la tabla categoria como fk para seleccionar categoria al momento de poblar la tabla plato
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    nom_plato = models.CharField(max_length=100, blank=False, null=False)
    descripcion_plato = models.CharField(max_length=200, blank=True, null=True)
    precio_plato = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    oferta_plato = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    foto_plato = models.ImageField(upload_to='img/plato', blank=True, null=True)

    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='idProveedor')

    fecha_publicacion = models.DateField(default=datetime.date.today)
    #banderas de actividad
    descuento_activo = models.BooleanField(default=True)
    plato_activo = models.BooleanField(default=True)

    def _str_(self):
        return self.nom_plato

# Creación de la tabla Pedido
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    comentario_pedido = models.CharField(max_length=200, blank=False, null=False)
    
    estado_pedido = models.CharField(max_length=100, blank=False, null=False)
    monto_pedido = models.DecimalField(default=1,max_digits=10, decimal_places=2, blank=False, null=False)
    cant_item = models.IntegerField(default=1,blank=False, null=False)
    fecha_pdido = models.DateField(default=datetime.date.today)
    retiro_local = models.BooleanField(default=True)

    plato = models.ForeignKey('Plato', on_delete=models.CASCADE, db_column='id_plato')
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    id_repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, db_column='id_repatidor', blank=True, null=True)
    id_agenda = models.ForeignKey('Agenda', on_delete=models.CASCADE, db_column='id_agenda',blank=True, null=True)

    def __str__(self):
        return f"Pedido {self.id_pedido} {self.estado_pedido}"
    
# creacion de la tabla itemPedido para agregar los platos al pedido    
class itemPedido(models.Model):
    plato = models.ForeignKey('Plato', on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)
    cantidad_item = models.IntegerField(default=0, blank=True, null=True)
    fecha_agregado = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Item del Pedido N°: {self.id}"
    
# Creación de la tabla Entregas
class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    estado_entrega = models.CharField(max_length=100, blank=False, null=False)
    comentario_entrega = models.CharField(max_length=100,blank=True, null=True)
    fecha_entrega = models.DateField(blank=False, null=False)
    hora_entrega = models.TimeField(blank=False, null=False)
    
    id_repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, db_column='id_repatidor')

    def __str__(self):
        return f"Entrega {self.id_entrega}"

# Creación de la tabla Agenda
class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    fecha_agendada= models.DateField(blank=False, null=False)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='id_pedido')

    def __str__(self):
        return f"Agenda {self.id_agenda}"