from django.db import models

# Create your models here.

#creacion de la tabla genero
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

#metodo que retorna el genero
def __str__(self):
    return str(self.genero)

#creacion de la tabla alumno
class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

#metodo que retorna el nombre y apellido paterno del alumno
def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

#creacion de la tabla ejemplo, project
class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    nombre     = models.CharField(max_length=20)
    fecha      = models.DateField(blank=False, null=False)
    descripcion= models.CharField(max_length=100)
    activo     = models.IntegerField()

#creacion de la tabla ejemplo, Task
class Task(models.Model):
    id_task   = models.AutoField(primary_key=True)
    nombre    = models.CharField(max_length=20)
    fecha     = models.DateField(blank=False, null=False)
    descripcion= models.CharField(max_length=100)
    id_project = models.ForeignKey('Project',on_delete=models.CASCADE, db_column='idProject')  
    activo    = models.IntegerField()

# Creación de la tabla Categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    des_categoria = models.CharField(max_length=100, blank=False, null=False)
    nom_categoria = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nom_categoria

# Creación de la tabla Cliente
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100, blank=False, null=False)
    rut_cliente = models.CharField(max_length=12, blank=False, null=False)
    saldo_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='pedido_id_pedido')

    def __str__(self):
        return self.nombre_cliente

# Creación de la tabla Entregas
class Entregas(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    desc_entrega = models.CharField(max_length=100, blank=False, null=False)
    fecha_entrega = models.DateField(blank=False, null=False)
    hora_entrega = models.TimeField(blank=False, null=False)

    def __str__(self):
        return self.desc_entrega

# Creación de la tabla Pedido
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    comentario_pedido = models.CharField(max_length=200, blank=False, null=False)
    plato = models.ForeignKey('Plato', on_delete=models.CASCADE, db_column='plato_id_plato')

    def __str__(self):
        return f"Pedido {self.id_pedido}"

# Creación de la tabla Plato
class Plato(models.Model):
    id_plato = models.CharField(max_length=20, primary_key=True)
    nom_plato = models.CharField(max_length=100, blank=False, null=False)
    desc_plato = models.CharField(max_length=200, blank=False, null=False)
    precio_plato = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    oferta_plato = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nom_plato

# Creación de la tabla Proveedor
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100, blank=False, null=False)
    plato = models.ForeignKey('Plato', on_delete=models.CASCADE, db_column='plato_id_plato')
    ventas = models.ForeignKey('Ventas', on_delete=models.CASCADE, db_column='ventas_id_venta')

    def __str__(self):
        return self.nombre_proveedor

# Creación de la tabla Repartidor
class Repartidor(models.Model):
    id_repartidor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12, blank=False, null=False)
    nombre_repartidor = models.CharField(max_length=100, blank=False, null=False)
    numero_telf = models.CharField(max_length=15, blank=False, null=False)
    entregas = models.ForeignKey('Entregas', on_delete=models.CASCADE, db_column='entregas_id_entrega')
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='pedido_id_pedido')

    def __str__(self):
        return self.nombre_repartidor

# Creación de la tabla Ventas
class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    monto_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    fecha_venta = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"Venta {self.id_venta}"
