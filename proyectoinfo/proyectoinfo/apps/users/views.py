from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login

# Create your views here.

def bienvenido(request):
	if request.user.is_authenticated:
		return render(request, 'bienvenido.html')
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

	return render(request, 'registrar.html', {'form' : form})

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
				return redirect('bienvenido/')

	return render(request, 'login.html', {'form' : form, 'div_clase' : 'test'},)


def logout(request):
	do_logout(request)
	return redirect('/')