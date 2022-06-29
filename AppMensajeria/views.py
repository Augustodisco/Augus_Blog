from django.shortcuts import render, redirect
from .models import *

def inicio(request):
    return render (request, 'AppMensajeria/inicio.html')

def sala(request, sala):
    usuario = request.GET('usuario')
    detalles_sala = Sala.objects.get(name=sala)
    return render (request, 'AppMensajeria/sala.html', {'usuario': usuario, 'sala': sala, 'detalles_sala': detalles_sala})

def chequearsala(request):
    sala = request.POST['nombre_sala']
    usuario = request.POST['usuario']

    if Sala.objects.filter(name=sala).exists():
        return redirect ('/'+ sala + '/?usuario='+ usuario) 
    else:
        nuevasala = Sala.objects.create(name=sala)
        nuevasala.save()
        return redirect ('/' + sala + '/?usuario='+ usuario)

def enviar (request):
    mensaje= request.POST['mensaje']
    usuario= request.POST['usuario']
    id_sala= request.POST['id_sala']

    nuevo_mensaje = Mensaje.objects.create(value=mensaje, user=usuario, sala=id_sala)
    nuevo_mensaje.save()
    return render (request, 'AppMensajeria/enviado.html')


# Create your views here.
