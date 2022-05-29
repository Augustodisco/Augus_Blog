from django.contrib import admin
from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('', inicio),
    path('about/', about, name='about'),
    path('miembros/', miembros, name='miembros'),
    path('educacion/',educacion , name='educacion'),
    path('proyectos/', proyectos, name='proyectos'),
    path('viajes/', viajes, name='viajes'),
]
