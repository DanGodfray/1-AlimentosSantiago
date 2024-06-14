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
    #alumnos = Alumno.objects.all()
    context ={"alumnos":obtenerListaAlumnos()}
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
    #generos = Genero.objects.all()
    context ={"generos":obtenerListaGeneros()}
    return render(request, 'alumnos/listaGeneros.html', context)

def crud(request):
    #retorna una consulta sql de todos los alumnos
    #alumnos = Alumno. objects.all()
    context ={"listaAlumnos":obtenerListaAlumnos()}
    return render(request, 'alumnos/alumnos_list.html', context)

def obtenerListaGeneros(): #para uptimizar codigo se puede usar esta funcion en vez de la funcion listaGeneros=Genero.objects.all()
    #retorna una consulta sql de todos los generos
    generos = Genero.objects.all()
    return generos

def obtenerListaAlumnos(): #para uptimizar codigo se puede usar esta funcion en vez de la funcion crud=Alumno. objects.all()
    #retorna una consulta sql de todos los alumnos
    alumnos = Alumno. objects.all()
    return alumnos

def alumnosAdd(request):
    #agregan alumnos a la base de datos
    #si el metodo es diferente a POST se retorna la vista alumnos_add.html
    
    try:
        if request.method != 'POST':
        #if request.method is not 'POST': //no funciona de esta manera
        #si no se ha enviado el formulario se retorna la vista alumnos_add.html para agregar un alumno
            
            #se define previamente un metodo que retorna todos los generos disponibles que seran mostrados en el dropdown: obtenerGenerosDropdown() 
            context ={"listaGeneros":obtenerListaGeneros()}
            #se renderiza la vista alumnos_add.html con los datos de la variable listaGeneros
            return render(request, 'alumnos/alumnos_add.html', context)
        
        else:
            
            rut             =request.POST['rut']
            nombre          =request.POST['nombre']
            apellido_paterno=request.POST['paterno']
            apellido_materno=request.POST['materno']
            fecha_nacimiento=request.POST['fechNac']
            genero          =request.POST['genero']
            telefono        =request.POST['telefono']
            email           =request.POST['email']
            direccion       =request.POST['direccion']
            activoTrue      ="1"
            #el objeto genero se obtiene de la tabla Genero y se almacena en la variable objetoGenero, para obtener todos los generos disponibles
            objetoGenero = Genero.objects.get(id_genero=genero)
            
            objetoAlumno = Alumno(rut=rut, 
                                nombre=nombre, 
                                apellido_paterno=apellido_paterno, 
                                apellido_materno=apellido_materno, 
                                fecha_nacimiento=fecha_nacimiento, 
                                id_genero=objetoGenero, 
                                telefono=telefono, 
                                email=email, 
                                direccion=direccion, 
                                activo=activoTrue)
            objetoAlumno.save()
            context ={"mensaje":"Alumno agregado correctamente"}
            #se renderiza el mensaje de error o exito en la vista alumnos_add.html
            return render(request, 'alumnos/alumnos_add.html', context)
    
    except Exception as e:
        #si ocurre un error se captura y se almacena en la variable e y se hace print en el terminal de python
        print(e)
        context ={"mensaje":"Error al agregar alumno", "listaGeneros":obtenerListaGeneros()}
        #se renderiza el mensaje de error o exito en la vista alumnos_add.html
        #se renderiza la vista alumnos_add.html con los datos de la lista listaGeneros
        return render(request, 'alumnos/alumnos_add.html', context)

def alumnos_del(request, pk):
    context={}
    try:
        #se obtiene el objeto alumno con el rut especifico "pk" es el nombre explicito en el modelo correspondiente
        alumno = Alumno.objects.get(rut=pk)
        alumno.delete()
        mensaje = "Alumno rut: %s, ha sido eliminado" % pk
        #alumnos = Alumno.objects.all()
        context ={"mensaje":mensaje, "alumnos":obtenerListaAlumnos()}
        return render(request, 'alumnos/alumnos_list.html', context)
        #return HttpResponse('Alumno eliminado: %s ' % pk)
    except Exception as e:
        mensaje = "Error al eliminar alumno: %s " % pk
        context ={"mensaje":mensaje, "alumnos":obtenerListaAlumnos()}
        return render(request, 'alumnos/alumnos_list.html', context)

def alumnos_findEdit(request, pk):
    
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        
        debug = type(alumno.id_genero.genero)
        debug2 = alumno.id_genero.genero
        print(f'esto es un debug de type: {debug}')
        print(f'esto es un debug de contenido: {debug2}')
        
        context={'listaAlumnos':alumno, 'listaGeneros':obtenerListaGeneros()}
        #la lista listaAlumnos se llena con el objeto alumno y la lista listaGeneros se llena con el metodo obtenerListaGeneros(), mediante la listaAlumnos se renderea en el template alumnos_edit.html
        
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context ={"mensaje":"Error al editar alumno"}
            return render(request, 'alumnos/alumnos_list.html', context)

def alumnosUpdate(request):
    if request.method == 'POST':
        rut             =request.POST['rut']
        nombre          =request.POST['nombre']
        apellido_paterno=request.POST['paterno']
        apellido_materno=request.POST['materno']
        fecha_nacimiento=request.POST['fechNac']
        genero          =request.POST['genero']
        telefono        =request.POST['telefono']
        email           =request.POST['email']
        direccion       =request.POST['direccion']
        activoTrue      ="1"
        
        #el objeto genero se obtiene de la tabla Genero y se almacena en la variable objetoGenero, para obtener todos los generos disponibles
        print(f'DEBUG1 POST el genero es: {genero}')
        #el post arroja el id del genero, se debe buscar el objeto genero con el id correspondiente
        
        objetoGenero = Genero.objects.get(id_genero=genero)
        #se obtiene el objeto genero con el id correspondiente
        
        print(f'DEBUG2 objetoGenero el genero es: {objetoGenero}')
        #este debug indica la totalidad del objeto genero el cual contiene el id y el genero
        
        objetoAlumno = Alumno(rut=rut, 
                                nombre=nombre, 
                                apellido_paterno=apellido_paterno, 
                                apellido_materno=apellido_materno, 
                                fecha_nacimiento=fecha_nacimiento, 
                                id_genero=objetoGenero, 
                                telefono=telefono, 
                                email=email, 
                                direccion=direccion, 
                                activo=activoTrue)
        objetoAlumno.save()
        #se almacena el objeto alumno en la base de datos
        
        mensaje = "Alumno rut: %s, ha sido actualizado" % rut
        #el mensaje de exito se almacena en la variable mensaje
        
        context ={"mensaje":mensaje, "listaAlumnos":objetoAlumno, "listaGeneros":obtenerListaGeneros()}
        #se renderiza el mensaje de error o exito en la vista alumnos_add.html
        
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        #si no se ha enviado el formulario se retorna la vista alumnos_add.html para agregar un alumno
        context ={"alumnos":obtenerListaAlumnos()}
        #se reinicia la vista alumnos_add.html con el metodo obtenerListaAlumnos() para obtener todos los alumnos
        
        return render(request, 'alumnos/alumnos_list.html', context)    

#----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-metodos ejemplo
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
