from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.forms import MiembrosFormulario
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def proyectos(request):
    return render(request, 'AppBlog/proyectos.html') 

def viajes(request):
    return render(request, 'AppBlog/viajes.html') 

def about(request):
    return render(request, 'AppBlog/about.html') 

def educacion(request):
    return render(request, 'AppBlog/educacion.html') 

def home (request):
    return render(request, 'AppBlog/home.html')

def miembros (request):
    if request.method == 'POST':
        miFormulario = MiembrosFormulario(request.POST)
        print (miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            miembro = Miembros (nombre=informacion['nombre'], apellido=informacion['apellido'], fechanacimiento=informacion['fechanacimiento'], miembro_desde=informacion['miembro_desde'])
            miembro.save()
            return render (request, 'AppBlog/formulariorecibido.html')
    else:
        miFormulario = MiembrosFormulario()
    return render (request, 'AppBlog/miembros.html', {'miFormulario':miFormulario})

def formulariorecibido (request):
    return render (request, 'AppBlog/formulariorecibido.html')

def buscar (request):
    if request.GET['apellido']:
        apellido = request.GET['apellido'] 
        miembro = Miembros.objects.filter(apellido=apellido)
        return render(request, 'AppBlog/rtabusqueda.html', {'miembro': miembro , 'apellido': apellido})
    else:
        respuesta="No enviaste un apellido, tratá de nuevo, te di una pista antes"
    
    return render (request, 'AppBlog/rtabusqueda.html', {'respuesta': respuesta})

def buscarescuela (request):
    if request.GET['lugar']:
        lugar = request.GET['lugar'] 
        educacion_esp = Educacion.objects.filter(lugar=lugar)
        return render(request, 'AppBlog/rtabusquedaescuela.html', {'educacion': educacion , 'lugar': lugar})
    else:
        respuesta="No enviaste una escuela correcta, tratá de nuevo, te di una pista antes"
    
    return render (request, 'AppBlog/rtabusquedaescuela.html', {'respuesta': respuesta})

def leerviajes (request):
    viajes = Viajes.objects.all()
    contexto = {'viajes': viajes}
    return render (request, 'AppBlog/viajes.html', contexto)

def leerproyectos (request):
    proyectos = Proyectos.objects.all()
    contexto = {'proyectos': proyectos}
    return render (request, 'AppBlog/proyectos.html', contexto)

def eliminarviajes (request, lugar):
    viaje = Viajes.objects.get(lugar = lugar)
    viaje.delete()
    viajes = Viajes.objects.all()
    contexto = {'viajes': viajes}
    return render (request, 'AppBlog/viajes.html', contexto)

def eliminarproyectos (request, nombre):
    proyecto = Proyectos.objects.get(nombre=nombre)
    proyecto.delete()
    proyectos = Proyectos.objects.all()
    contexto = {'proyectos': proyectos}
    return render (request, 'AppBlog/proyectos.html', contexto)


#--------------------------------------AVATAR--------------------------------------
"""def editarperfil(request):

    #usuario=request.user
    #if request.method == 'POST':
        #formulario=UserEditForm(request.POST, instance=usuario)
        #if formulario.is_valid():
            #informacion=formulario.cleaned_data
            #usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'AppBlog/home.html', {'usuario': usuario, 'mensaje':'PERFIL CREADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppBlog/editarperfil.html', {'formulario': formulario, 'usuario': usuario.username})"""