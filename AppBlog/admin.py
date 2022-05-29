from django.contrib import admin

from django.contrib import admin
from .models import Educacion, Miembros, Proyectos, Viajes

# Register your models here.
admin.site.register(Viajes)
admin.site.register(Proyectos)
admin.site.register(Miembros)
admin.site.register(Educacion)