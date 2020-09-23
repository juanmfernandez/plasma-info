from django.contrib import admin
from .models import Noticia
from .models import *
#---< Lo siguiente es para tener botones para importar y exportar en admin >---
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo','autor','fecha_creacion')
	list_filter = ('autor',)
		
#Para poder personalizar nuestro admin.
#Ahora agregamos una clase de botones para nuestro admin
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    #Añadimos un buscador dentro de categorias, el filtro es nombre, pero puede cualquiera que nostros definamos
    #Para esto es necesario que en admin.site.register pases por parametro la categoria y esta clase.

    list_display = ('nombre', 'estado',)
    resource_class = CategoriaResource #Esto es para el boton importar/exportar

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['apellidos', 'nombres', 'fecha_union', 'donante',] #Esto es para el buscador
    list_display = ('apellidos', 'nombres', 'fecha_union', 'donante',) #Esto es para la barra de detalles
    resource_class = AutorResource #Esto es para el boton importar/exportar

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'autor', 'fecha_creacion', 'categoria', 'verificado',]
    list_display = ('titulo', 'autor', 'fecha_creacion', 'categoria', 'verificado',)
    resource_class = PostResource


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Comentario)
admin.site.register(Post, PostAdmin)
admin.site.register(Noticia, NoticiaAdmin)

