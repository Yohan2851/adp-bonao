from django.db import models
from django.contrib.auth.models import AbstractUser

from custonUser.settings import MEDIA_URL, STATIC_URL
from ubicaciones.models import Distrito, Escuela, Cargo


# Create your models here.

class User(AbstractUser):
    picture = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
    cedula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    ESTADO_CIVIL_CHOICES = [
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo'),
    ]
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES,blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    codigo_de_cuenta = models.CharField(max_length=4, unique=True, blank=True, null=True)

    # Relación con el modelo Distrito
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, related_name='miembros', null=True, blank=True)
    # Relación con el modelo Escuela
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='miembros', null=True, blank=True)

    # Relación con el modelo Cargo
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='miembros', null=True, blank=True)

    def get_image(self):
        if self.picture:
            return '{}{}'.format(MEDIA_URL, self.picture)

        return '{}{}'.format(STATIC_URL, 'img/person-2.jpg')