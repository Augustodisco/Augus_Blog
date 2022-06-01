from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.forms import MiembrosFormulario
from .models import Miembros


# Create your views here.

def inicio(request):
    return render(request, 'AppBlog/inicio.html') 

def miembros(request):
    return render(request, 'AppBlog/miembros.html') 

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

def miembrosformulario (request):
    if request.method == 'POST':
        
        miFormulario=MiembrosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            miembro=Miembros(nombre=informacion['nombre'],apellido=informacion['apellido'],fechanacimiento=informacion['fechanacimiento'],miembro_desde=informacion['miembro_desde'])
            miembro.save()
            return render(request, 'AppBlog/home.html')
    else:
        miFormulario=MiembrosFormulario()    
    return render(request, 'AppBlog/miembrosformulario.html', {'formulario': miFormulario})

def busquedamiembros(request):
    return render (request, 'AppBlog/busquedamiembros.html')

def buscar(request):
    if request.GET['apellido']:
        apellido= request.GET['apellido']
        miembros= Miembros.objects.filter(miembros=miembros)
        return render (request, 'AppBlog/rtabusqueda.html', {"miembros":miembros , "apellido": apellido})
    else:
        respuesta="No enviaste datos"
    return(HttpResponse)