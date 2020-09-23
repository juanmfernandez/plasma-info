from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField #Esto me permite editar el post con ckeditor, mas configuraciones en settings/base
from ..users.models import Usuario

#Los modelos son una tabla en nuestra BD
#Modelo de categoria para nuestros post (La categoria la crea el admin)

class Noticia(models.Model):

	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.fecha_publicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

class Meta:
	verbose_name = ("Noticia")
	verbose_name_plural = ("Noticias")
		
class Categoria(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la categoria', max_length=100, null= False, blank=False)
    estado= models.BooleanField('Categoria activada/Categoria no activada', default=True)
    fecha_creacion= models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    #Para fecha de creacion tenemos auto_now indica que no queremos que la categorai cambie de fecha cada vez que actualicemos sus datos
    # En cambio con auto_now_add indicamos que se cree la fecha una sola vez y es cuando creamos la categoria

    class Meta: #Forma en que se va a ver en admin al modelo
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self): #Muestra los datos que nosotros queremos en el admin
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=255, null= False, blank=False)
    apellidos = models.CharField('Apellidos', max_length=255, null=True, blank=True)
    #Parametros opcionales
    email = models.EmailField('Email', null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    donante = models.BooleanField('Donante/Futuro donante', default=False)
    fecha_union = models.DateField('Fecha de alta', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name= 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        #return "{0} - {1} - {2} - {3}".format(self.apellidos, self.nombres, self.fecha_union, self.donante)
        return "{0}, {1}".format(self.apellidos, self.nombres)
        

#Los post que se pueden acceder desde home.
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length= 90, blank= False, null = False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    contenido = RichTextField('Contenido') #Esto lo hicimos con ckeditior
    descripcion = models.CharField('Descripcion', max_length=110, blank=False, null=False)
    imagen = models.URLField(max_length = 255, blank=False, null=False) #Renderiza imagen.
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE) #Hace referencia a que un autor puede crear muchos post
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    verificado = models.BooleanField('Post Verificado', default=False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return "{0} - {1} - {2} - {3} - {4}".format(self.titulo, self.autor, self.fecha_creacion, self.categoria ,self.verificado)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comentarios')
    contenido = models.TextField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return self.contenido

    def approve(self):
        self.aprobado = True
        self.save()

    class Meta:
        verbose_name = ('Comentario')
        verbose_name_plural = ('Comentarios')
    
    def comentarios_aprobados(self):
        return self.comentarios.filter(aprobado=True)

