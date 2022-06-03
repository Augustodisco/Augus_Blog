from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.forms import MiembrosFormulario,  UserRegistrationForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

#-------------------------------------LOGIN------------------------------------------------
def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
            user=authenticate(username=usuario, password=clave) 
            if user is not None:
                 login(request, user)
                 return render (request, 'AppBlog/rtalogin.html', {'usuario':usuario, 'mensaje':'Bienvenido al sistema'})
            else:
                return render(request,'AppBlog/rtalogin.html', {'mensaje':'Incorrecto vuelva a loguearse'})     
        else:
            return render (request, 'AppBlog/rtalogin.html', {'mensaje':'Formulario incorrecto, vuelva a ingresar otro'})
    formulario=AuthenticationForm()
    return render (request, 'AppBlog/login.html', {'formulario':formulario})

def rtalogin (request):
    return render (request, 'AppBlog/rtalogin.html')

def register(request):
    if request.method == 'POST':
        formulario =UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render (request, 'AppBlog/rtalogin.html', {'mensaje': f'Usuario: {username} creado exitosamente'})
        else:
             return render (request, 'AppBlog/rtalogin.html', {'mensaje':'No se pudo crear intente nuevemante'})
    else:
        formulario= UserRegistrationForm()
        return render (request, 'AppBlog/register.html', {'formulario':formulario})



