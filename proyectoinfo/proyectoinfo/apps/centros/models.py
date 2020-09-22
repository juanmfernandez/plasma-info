from django.db import models


class CentroHabilitado(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    nro_tel = models.IntegerField()
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, blank=True, null=True, default = 'Resistencia')
    #direccion = GeopositionField()
    horario_aten = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("CentroHabilitado")
        verbose_name_plural = ("CentrosHabilitados")