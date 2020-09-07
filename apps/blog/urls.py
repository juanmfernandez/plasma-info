from django.urls import path
from . import views

urlpatterns = [
	path('', views.listar_noticias, name='lista'),
]