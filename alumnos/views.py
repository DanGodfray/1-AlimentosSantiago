from django.shortcuts import render
from .models import Genero, Alumno

#se importan modelos ejemplo de las clases project y task
from .models import Project, Task

#se debe importar el objeto al cual se le va a hacer referencia en la vista y se le almacena los datos captados en una variable, esto es para captura de datos en el url mismo
from django.http import HttpResponse, JsonResponse

# Create your views here.
# esta es la vista que se llama cuando se accede a la url y metodos asociados a entrara esos urls

def index(request):
    alumnos = Alumno.objects.all()
    context ={"alumnos":alumnos}
    #retorna la vista index.html con los datos de la variable alumnos
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    #retorna una consulta sql de todos los alumnos
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context ={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def listaGeneros(request):
    #retorna una consulta sql de todos los generos
    generos = Genero.objects.all()
    context ={"generos":generos}
    return render(request, 'alumnos/listaGeneros.html', context)

#----metodos ejemplo
# esta es una vista que recibe un parametro usuario e imprime el nombre del usuario

def indexUser(request, user):  
    #esto es un ejemplo de debug por terminal en python, se puede ver al momento de acceder a la url o refrescar la pagina.
    print(f"El usuario es tipo: {type(user)}")
    return HttpResponse("<h2>Hola %s</h2>" % user)

def projects(request):
    #se convierte en el objeto Project y se almacena en la variable projects
    projects = list(Project.objects.values()) 
    #return HttpResponse('projects')
    return JsonResponse(projects, safe=False)



def tasks(request):
    return HttpResponse('tasks')