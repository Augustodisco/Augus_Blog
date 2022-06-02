from django.contrib import admin
from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('educacion/',educacion , name='educacion'),
    path('proyectos/', proyectos, name='proyectos'),
    path('viajes/', viajes, name='viajes'),
    path('miembros/',miembros, name='miembros'),
    path('formulariorecibido/',formulariorecibido, name='formulariorecibido'),
    path('buscar/', buscar),
    path('leerviajes/', leerviajes, name='leerviajes'),
    path('leerproyectos/', leerproyectos, name='leerproyectos'),
  
    
]
