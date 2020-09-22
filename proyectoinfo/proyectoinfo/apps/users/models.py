from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni =  models.CharField(max_length=9, null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)