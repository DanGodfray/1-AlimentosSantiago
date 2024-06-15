from django.contrib import admin
from .models import Genero, Alumno

#se debe importar los modelos que se van a registrar
from .models import Project, Task

# Register your models here.

admin.site.register(Genero)
admin.site.register(Alumno)

#estos son los modelos ejemplo que se pueden regiatrar en la pagina del admin
admin.site.register(Project)
admin.site.register(Task)