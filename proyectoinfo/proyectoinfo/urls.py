"""ProyectoInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .apps.users import views
from .settings import base
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #import this

#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyectoinfo.apps.blog.urls')),
    path('', include('proyectoinfo.apps.centros.urls')),
    path('', include('proyectoinfo.apps.users.urls')),
    path('bienvenido/', views.bienvenido),
    path('registrar/', views.crearUsuario),
    path('login/', views.login),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
        name='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
        name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
        name='password_reset_complete'), 
] + static(base.STATIC_URL, document_root=base.STATIC_ROOT)
