from django.shortcuts import render

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

