from django.contrib import admin
from .models import Noticia

# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo','autor','fecha_creacion')
	list_filter = ('autor',)
		

admin.site.register(Noticia, NoticiaAdmin)
