from django.shortcuts import render

# Create your views here.

def listar_noticias(request):
	return render(request, 'lista_noticias.html', {})