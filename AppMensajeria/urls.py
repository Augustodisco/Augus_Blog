from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('<str:sala>/', views.sala, name='sala'), 
    path('chequearsala', views.chequearsala, name='chequearsala'),
    path('enviar/', views.enviar, name='enviar')
    





]
