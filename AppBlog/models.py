from django.db import models

# Create your models here.

class Viajes(models.Model):
    destino=models.CharField(max_length=50)
    año=models.IntegerField()

class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    año=models.IntegerField()

class Miembros(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechanacimiento=models.CharField(max_length=10)
    miembro_desde=models.IntegerField()

class Educacion(models.Model):
    lugar=models.CharField(max_length=50)
    desde_cuando=models.CharField(max_length=50)

