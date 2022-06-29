from django.contrib import admin
from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView
from django import views



urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('educacion/',educacion , name='educacion'),
    path('proyectos/', proyectos, name='proyectos'),
    path('formproyectosrecibido/', formproyectosrecibido, name='formproyectosrecibido'),
    path('eliminar_proyecto/<id>', eliminarproyectos, name='eliminar_proyecto'),
    path('editar_proyecto/<id>/', editarproyecto, name='editar_proyecto'),
    path('viajes/', viajes, name='viajes'),
    path('formviajesrecibido/', formviajesrecibido, name='formviajesrecibido'),
    path('eliminar_viaje/<id>', eliminarviajes, name='eliminar_viajes'),
    path('editar_viaje/<id>/', editarviajes, name='editar_viaje'),
    path('miembros/',miembros, name='miembros'),
    path('formulariorecibido/',formulariorecibido, name='formulariorecibido'),
    path('buscar/', buscar),
    path('buscarescuela/',buscarescuela),
    

    path('login/', login_request, name='login'),
    path('rtalogin/', rtalogin, name='rtalogin'),
    path('register/', register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('editarperfil/',editarperfil, name='editarperfil')
]
