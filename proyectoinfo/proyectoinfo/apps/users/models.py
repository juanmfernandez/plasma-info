from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django import forms

class Usuario(AbstractUser, models.Model):
    first_name = models.CharField(verbose_name="Nombres", max_length=50, blank=False)
    last_name = models.CharField(verbose_name="Apellidos", max_length=50, blank=False)
    dni =  models.CharField(verbose_name="DNI", max_length=9, null=True, blank=True, unique=True)
    email =  models.EmailField(unique=True)
    fecha_nac = models.DateField(verbose_name="Fecha nacimiento", null=True, blank=True)
    grupo_sanguineo = models.CharField(verbose_name="Grupo", max_length=3, null=True, blank=True)
    factor_rh = models.CharField(verbose_name="Factor Rh", max_length=2, null=True, blank=True)
    es_donante = models.BooleanField('Donante/Futuro donante', default=False)


    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return "{} - {} - {} -{}".format(self.last_name,self.first_name,self.username,self.email,self.dni)