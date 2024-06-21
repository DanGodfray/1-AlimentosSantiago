# Creación de la tabla Entregas
class Entregas(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    estado_entrega = models.CharField(max_length=100, blank=False, null=False)
    comentario_entrega = models.CharField(max_length=100,blank=True, null=True)
    fecha_entrega = models.DateField(blank=False, null=False)
    hora_entrega = models.TimeField(blank=False, null=False)
    
    id_repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, db_column='id_repatidor')

    def __str__(self):
        return f"Entrega {self.id_entrega}"

# Creación de la tabla Pedido
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    comentario_pedido = models.CharField(max_length=200, blank=False, null=False)
    
    estado_pedido = models.CharField(max_length=100, blank=False, null=False)
    monto_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    cant_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    fecha_venta = models.DateField(blank=False, null=False)
    retiro_local = models.BooleanField(default=True)

    plato = models.ForeignKey('Plato', on_delete=models.CASCADE, db_column='id_plato')
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    id_repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, db_column='id_repatidor', blank=True, null=True)
    id_agenda = models.ForeignKey('Agenda', on_delete=models.CASCADE, db_column='id_agenda',blank=True, null=True)


    def __str__(self):
        return f"Pedido {self.id_pedido}"

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    fecha_agendada= models.DateField(blank=False, null=False)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='id_pedido')

    def __str__(self):
        return f"Agenda {self.id_agenda}"