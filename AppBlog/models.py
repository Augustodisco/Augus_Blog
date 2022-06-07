from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Viajes(models.Model):
    destino=models.CharField(max_length=50)
    año=models.IntegerField()

    def __str__(self):
          return self.destino



class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    año=models.IntegerField()

    def __str__(self):
          return self.nombre

class Miembros(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechanacimiento=models.CharField(max_length=10)
    miembro_desde=models.IntegerField()

    def __str__(self):
          return self.nombre+" "+self.apellido

class Educacion(models.Model):
    lugar=models.CharField(max_length=50)
    desde_cuando=models.CharField(max_length=50)

    def __str__(self):
          return self.lugar

class Avatar (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)
