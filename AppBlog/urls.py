from django.contrib import admin
from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('miembros/', miembros, name='miembros'),
    path('educacion/',educacion , name='educacion'),
    path('proyectos/', proyectos, name='proyectos'),
    path('viajes/', viajes, name='viajes'),
    path('miembrosformulario/', miembrosformulario, name='miembrosFormulario'),
    path('busquedamiembros/', busquedamiembros, name='busquedamiembros'),
    path('buscar/', buscar),
]
