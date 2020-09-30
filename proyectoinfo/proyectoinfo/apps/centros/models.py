from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField


class EnableCenter(models.Model):
    name = models.CharField(verbose_name="Nombre del centro", max_length=200)
    mail = models.CharField(verbose_name="E-mail", max_length=200)
    phone_num = models.IntegerField(verbose_name="Telefono")
    address = models.CharField(verbose_name="Dirección", max_length=200)
    location = PlainLocationField(verbose_name="Ubicación en mapa", based_fields=['city'], zoom=7)
    business_hours = models.CharField(verbose_name="Horario de atención", max_length=200)
