from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario
from django.views.generic.list import ListView
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators  import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def bienvenido(request):
	if request.user.is_authenticated:
		return render(request, 'registration/bienvenido.html')
	return redirect('/login')


def registrar(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				do_login(request, user)
				return redirect('/')
	return render(request, 'registration/registrar.html', {'form' : form})


def crearUsuario(request):
    if request.method == 'POST': #Para registrarse
        usuario_form = UsuarioForm(request.POST)
        if usuario_form .is_valid():
            usuario_form.save()
            messages.success(request, 'Se ha registrado correctamente.')
            return redirect('/login') #En index debe ir el template que permita crear post, desloguarte, etc.
    else:
        usuario_form = UsuarioForm()
    return render(request, 'registration/registrar.html',{'usuario_form':usuario_form})

def login(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request, user)
				if request.GET.get('next'):
					return redirect(request.GET.get('next'))
				return redirect('/')
				#return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	return render(request, 'registration/login.html', {'form' : form, 'div_clase' : 'test'},)


def logout(request):
	do_logout(request)
	return redirect('/')

class ListarDonantes(LoginRequiredMixin, ListView):
	login_url = 'login'
	model = Usuario
	template_name = 'users/lista_donantes.html'
	context_object_name = "donantes"
	
	def get_queryset(self):
		donantes = Usuario.objects.all().filter(es_donante=True)
		return donantes
