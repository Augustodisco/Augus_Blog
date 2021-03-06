from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class MiembrosFormulario (forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    fechanacimiento=forms.CharField(max_length=10)
    miembro_desde=forms.IntegerField()

class ProyectosFormulario (forms.Form):
    nombre=forms.CharField(max_length=50)
    año=forms.IntegerField()

class ViajesFormulario (forms.Form):
    destino=forms.CharField(max_length=50)
    año=forms.IntegerField()


class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Contraeña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username', 'email', 'password1','password2')
        help_texts= { k:"" for k in fields}

        
class UserEditForm(UserCreationForm):
    email= forms.EmailField(label='Modificar Email')
    password1= forms.CharField(label='Modificar Contraeña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    last_name=forms.CharField(label='Modificar Apellido')
    first_name=forms.CharField(label='Modificar Nombre')
    
    class Meta:
        model=User
        fields=('email', 'password1','password2', 'last_name','first_name')
        help_texts= { k:"" for k in fields}