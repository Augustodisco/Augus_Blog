from django import forms

class EnviarMensaje (forms.Form):
    emisor=forms.all_valid()
    receptor=forms.all_valid()
    mensaje=forms.all_valid()