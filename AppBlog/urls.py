from django.contrib import admin
from django.urls import path
from .views import *
from AppBlog import views

urlpatterns = [
    path('', views.inicio),
]
