from django.shortcuts import render

# Create your views here.
def registrar_centro(request):
	#if request.user.is_authenticated:
	return render(request, 'registrar_centro.html')
	#return redirect('/login')

def mapa(request):
	return render(request, 'mapa.html')
	