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