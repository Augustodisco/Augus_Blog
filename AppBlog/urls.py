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
    path('viajes/', viajes, name='viajes'),
    path('miembros/',miembros, name='miembros'),
    path('formulariorecibido/',formulariorecibido, name='formulariorecibido'),
    path('formviajesrecibido/', formviajesrecibido, name='formviajesrecibido'),
    path('buscar/', buscar),
    path('buscarescuela/',buscarescuela),
    

    path('login/', login_request, name='login'),
    path('rtalogin/', rtalogin, name='rtalogin'),
    path('register/', register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('editarperfil/',editarperfil, name='editarperfil')
]
