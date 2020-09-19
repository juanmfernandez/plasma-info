from django.db import models
from django.utils import timezone

# Create your models here.

class CentroHabilitado(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    nro_tel = models.IntegerField()
    direccion = models.CharField(max_length=50)
    long_lat = models.CharField(max_length=50, blank=True, null=True, default = '0000')
    ciudad = models.CharField(max_length=50, blank=True, null=True, default = 'Resistencia')
    horario_aten = models.CharField(max_length=50)

    class Meta:
	    verbose_name = ("CentroHabilitado")
	    verbose_name_plural = ("CentrosHabilitados")

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default = timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    class Meta:
	    verbose_name = ("Post")
	    verbose_name_plural = ("Posts")

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    contenido = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    fecha_hora = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = ('Comentario')
        verbose_name_plural = ('Comentarios')