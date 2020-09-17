from django.db import models
from django.utils import timezone

# Create your models here.

class CentroHabilitado(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    nro_tel = models.IntegerField(max_length=50)
    direccion = models.CharField(max_length=50)
    horario_aten = models.CharField(max_length=50)

    class Meta:
	    verbose_name = ("CentroHabilitado")
	    verbose_name_plural = ("CentrosHabilitados")

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contenido = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)

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

    class Meta:
        verbose_name = ('Comentario')
        verbose_name_plural = ('Comentarios')