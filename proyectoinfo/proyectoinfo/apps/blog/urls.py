from django.urls import path
from . import views
from .views  import (blog,informacion,cat_recomendacion,cat_ayuda,cat_experiencia,
    cat_noticia,cat_consultas,detallePost,crearAutor)

urlpatterns = [
    path('',views.home.as_view(), name='home'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('blog/',blog, name='blog'),
    path('informacion',informacion, name='informacion'),
    path('crear_autor',crearAutor,name='crear_autor'),
    path('cat_recomendacion',cat_recomendacion, name='cat_recomendacion'),
    path('cat_ayuda',cat_ayuda, name='cat_ayuda'),
    path('cat_experiencia',cat_experiencia, name='cat_experiencia'),
    path('cat_noticia',cat_noticia, name='cat_noticia'),
    path('cat_consultas',cat_consultas, name='cat_consultas'),
    #path('<slug:slug>',detallePost, name='detallePost'), #Esta siempre va ultima.
    #path('detalle/<slug:pk>', DetalleNoticia.as_view(), name='detalle'),
    path('detalle/<slug:slug>',detallePost, name='detallePost'), #Esta siempre va ultima.
    path('detalle/',blog, name='blog'),
    path('detalle/<slug:slug>/comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('comentario/<slug:pk>/aprobar/', views.aprobar_comentario, name='aprobar_comentario'),
    path('comentario/<slug:pk>/borrar/', views.borrar_comentario, name='borrar_comentario'),
]
