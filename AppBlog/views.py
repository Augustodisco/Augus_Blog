from asyncio.windows_events import NULL
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.forms import MiembrosFormulario, ProyectosFormulario, ViajesFormulario, UserRegistrationForm, UserEditForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def about(request):
    return render(request, 'AppBlog/about.html') 

def educacion(request):
    return render(request, 'AppBlog/educacion.html') 

@login_required
def home (request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppBlog/home.html', {'url' :avatar[0].imagen.url} )

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
        if len(miembro) == 0:
            respuesta="No se encontró un apellido correcto, tratá de nuevo, te di una pista antes"
            return render(request, 'AppBlog/rtabusqueda.html', {'miembro': miembro , 'apellido': apellido, 'respuesta': respuesta})
        else:
            return render(request, 'AppBlog/rtabusqueda.html', {'miembro': miembro , 'apellido': apellido})
    else:
        respuesta="No enviaste un apellido, tratá de nuevo, te di una pista antes"
    
    return render (request, 'AppBlog/rtabusqueda.html', {'respuesta': respuesta})

def buscarescuela (request):
    if request.GET['lugar']:
        lugar = request.GET['lugar'] 
        edu= Educacion.objects.filter(lugar=lugar)
        if len(edu) == 0:
            respuesta="No se encontró una escuela correcta, tratá de nuevo, te di una pista antes"
            return render(request, 'AppBlog/rtabusquedaescuela.html', {'edu': edu , 'lugar': lugar, 'respuesta':respuesta})
        else:
            return render (request, 'AppBlog/rtabusquedaescuela.html', {'edu': edu , 'lugar': lugar})
    else:
        respuesta="No enviaste ninguna escuela, tratá de nuevo, te di una pista antes"
    
    return render (request, 'AppBlog/rtabusquedaescuela.html', {'respuesta': respuesta})

#------------------------------------------CRUD COMPLETO PROYECTO Y VIAJES-----------------------------------------------------

def proyectos(request):
    if request.method == 'POST':
        miFormulario = ProyectosFormulario(request.POST)
        print (miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proyecto = Proyectos (nombre=informacion['nombre'], año=informacion['año'])
            proyecto.save()
            return render (request, 'AppBlog/formproyectosrecibido.html')
    else:
        miFormulario = ProyectosFormulario()
    proyectos = Proyectos.objects.all()
    contexto = {'proyectos': proyectos, 'miFormulario':miFormulario}
    return render (request, 'AppBlog/proyectos.html', contexto)

def formproyectosrecibido(request):
    return render (request, 'AppBlog/formproyectosrecibido.html')

def eliminarproyectos (request,id):   
    proyecto = Proyectos.objects.get(id=id)
    proyecto.delete()
    return proyectos(request)  

def viajes (request):
    if request.method == 'POST':
        miFormulario = ViajesFormulario(request.POST)
        print (miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            viaje = Viajes (destino=informacion['destino'], año=informacion['año'])
            viaje.save()
            return render (request, 'AppBlog/formviajesrecibido.html')
    else:
        miFormulario = ViajesFormulario()
    viajes = Viajes.objects.all()
    contexto = {'viajes': viajes, 'miFormulario':miFormulario}
    return render (request, 'AppBlog/viajes.html', contexto)

def formviajesrecibido (request):
    return render (request, 'AppBlog/formviajesrecibido.html')

def eliminarviajes (request,id):   
    viaje = Viajes.objects.get(id=id)
    viaje.delete()
    return viajes(request)  

def editarproyecto(request,id):
    proyecto= Proyectos.objects.get(id=id)
    if request.method == 'POST':
        miFormulario=ProyectosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            proyecto.nombre=informacion['nombre']
            proyecto.año=informacion['año']
            proyecto.save()
            proyectos=Proyectos.objects.all()
            contexto= {'proyectos':proyectos}
            return render (request, 'AppBlog/proyectos.html', contexto)
    else:
        miFormulario=ProyectosFormulario(initial={'nombre':proyecto.nombre, 'año':proyecto.año})
    return render(request, 'AppBlog/editarproyecto.html', {'miFormulario':miFormulario, 'id':id})  

def editarviajes(request,id):
    viaje= Viajes.objects.get(id=id)
    if request.method == 'POST':
        miFormulario=ViajesFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            viaje.destino=informacion['destino']
            viaje.año=informacion['año']
            viaje.save()
            viajes=Viajes.objects.all()
            contexto= {'viajes':viajes}
            return render (request, 'AppBlog/viajes.html', contexto)
    else:
        miFormulario=ViajesFormulario(initial={'destino':viaje.destino, 'año':viaje.año})
    return render(request, 'AppBlog/editarviaje.html', {'miFormulario':miFormulario, 'id':id})

#--------------------------------------AVATAR--------------------------------------

def editarperfil(request):

    usuario=request.user
    if request.method == 'POST':
        miFormulario=UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            usuario.email=informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.set_password(informacion['password2'])
            usuario.save()

            return render(request, 'AppBlog/home.html')
    else:
        miFormulario=UserEditForm(instance=usuario)
    return render(request, 'AppBlog/editarperfil.html', {'miFormulario': miFormulario, 'usuario': usuario.username})


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
        Formulario = UserRegistrationForm(request.POST)
        if Formulario.is_valid():
            username=Formulario.cleaned_data['username']
            Formulario.save()
            return render (request, 'AppBlog/home.html')
        else:
             return render (request, 'AppBlog/register.html',{'Formulario': Formulario, 'mensaje':'No se pudo crear intente nuevemante'})
    else:
        Formulario= UserRegistrationForm()
        return render (request, 'AppBlog/register.html', {'Formulario':Formulario})



