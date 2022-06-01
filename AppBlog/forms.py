from django import forms

class MiembrosFormulario (forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    fechanacimiento=forms.CharField(max_length=10)
    miembro_desde=forms.IntegerField()