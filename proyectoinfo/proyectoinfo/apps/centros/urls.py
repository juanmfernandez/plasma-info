from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registrar_centro, mapa

urlpatterns = [
	path('registrar_centro/', registrar_centro, name='registrar_centro'),
	path('mapa/',  mapa, name='mapa')
	
]

