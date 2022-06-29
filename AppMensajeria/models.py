from django.db import models
from datetime import datetime

class Mensaje (models.Model):
    emisor=models.CharField(max_length=200000000)
    receptor=models.CharField(max_length=200)
    cuerpo=models.CharField(max_length=200000000)
    fecha=models.DateTimeField(default=datetime.now, blank=True)
    

class Sala (models.Model):
    nombre=models.CharField(max_length=200)

# Create your models here.
