from django.shortcuts import render
from .models import Genero, Alumno

#se importan modelos ejemplo de las clases project y task
from .models import Project, Task

#manejo de errores en caso que no se encuentre un objeto
from django.shortcuts import get_object_or_404

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

def crud(request):
    #retorna una consulta sql de todos los generos
    alumnos = Alumno. objects.all()
    context ={"alumnos":alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    #retorna una consulta sql de todos los generos
    if request.method is not 'POST':
        
        generos = Genero.objects.all()
        context ={"generos":generos}
        return render(request, 'alumnos/alumnos_add.html', context)

#----metodos ejemplo
# esta es una vista que recibe un parametro usuario e imprime el nombre del usuario

def indexUser(request, user):  
    #esto es un ejemplo de debug por terminal en python, se puede ver al momento de acceder a la url o refrescar la pagina.
    print(f"El usuario es tipo: {type(user)}")
    return HttpResponse("<h2>Hola %s</h2>" % user)

    #esto es un ejemplo de consulta usando jason y se retorna los datos de la tabla project
def projects(request):
    #se convierte en el objeto Project y se almacena en la variable projects
    projects = list(Project.objects.values()) 
    #return HttpResponse('projects')
    return JsonResponse(projects , safe=False)

#ejemplo consulta de la tabla task con un id especifico
def tasks(request,id):
    #se obtiene el objeto task con el id especifico "id_task" es el nombre explicito en el modelo correspondiente
    
    #task = Task.objects.get(id_task=id)
    task = get_object_or_404(Task, id_task=id)
    return HttpResponse('task: %s ' % task.nombre)

#ejemplo consulta de la tabla task con un id especifico
def tasks2(request, nombre):
    #se obtiene el objeto task con el id especifico "id_task" es el nombre explicito en el modelo correspondiente
    
    #task = Task.objects.get(id_task=id)
    task2 = get_object_or_404(Task, nombre=nombre)
    return HttpResponse('task: %s ' % task2.nombre)
