from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login, ListarDonantes, logout, crearUsuario

urlpatterns = [
	#path('login/', auth_views.LoginView.as_view(), {'template_name':"registration/login.html"}, name='login'),
	path('logout/',  logout, name='logout'),	
	path('lista_donantes/', ListarDonantes.as_view(), name='lista_donantes'),
	path('registrar/', crearUsuario, name='registrar'),

	
	#"""
	#path('accounts/', include('django.contrib.auth.urls')),
	#path('password_change/', password_change [name='password_change'])
	#path('password_change_done/', password_change_done [name='password_change_done'])
	#path('password_reset/', password_reset [name='password_reset'])
	#path('password_reset_done/', password_reset_done$ [name='password_reset_done'])
	#path('reset/', accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm'])
	#path('password_reset_complete/', password_reset_complete [name='password_reset_complete'])
	#"""
]

