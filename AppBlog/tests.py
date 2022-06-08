from django.test import TestCase
from .models import *

@TestCase.mark.django_db
def test_miembros(TestCase):
    miembro = miembro.objects.create_miembro (
    nombre="Pedrito",
    apellido="Gonzalez",
    fechanacimiento ="17-06-200000",
    miembro_desde=2018
    )
    assert len(miembro.fechanacimiento) == 10

# Create your tests here.
