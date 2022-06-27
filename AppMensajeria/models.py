from django.db import models

class Mensaje (models.Model):
    emisor=models.CharField(max_length=200)
    receptor=models.CharField(max_length=200)
    cuerpo=models.CharField(max_length=200)
    campo_leido=models.BooleanField()




# Create your models here.
