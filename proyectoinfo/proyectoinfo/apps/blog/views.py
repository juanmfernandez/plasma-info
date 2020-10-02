from django.shortcuts import render, redirect
from .forms import AutorForm, ComentarioForm
from .models import Post,Categoria, Comentario
from ..centros.models import EnableCenter
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

def blog(request):
    queryset= request.GET.get("buscar")
    post = Post.objects.filter(verificado = True)
    #Acontinuacion de esta linea se escribe el codigo para listar los post en la pagina principal
    if queryset:
        post = Post.objects.filter(
                Q(titulo__icontains = queryset) | 
                Q(descripcion__icontains = queryset)
            ).distinct()
    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'blog/index.html',{'post':post}) #Con el render listamos los post, pasando por parametro (3er parametro)



def cat_recomendacion(request):
    queryset= request.GET.get("buscar")
    #Para filtrar post de una categoria determinada
    post= Post.objects.filter(categoria= Categoria.objects.get(nombre = 'Recomendacion') )
    if queryset:
        post = Post.objects.filter(
                Q(titulo__icontains = queryset) | 
                Q(descripcion__icontains = queryset)
            ).distinct()
    return render(request, 'blog/Cat_Recomendacion.html',{'post':post})

def cat_ayuda(request):
    queryset= request.GET.get("buscar")
    post=Post.objects.filter(categoria=Categoria.objects.get(nombre='Ayuda'))
    if queryset:
        post = Post.objects.filter(
                Q(titulo__icontains = queryset) | 
                Q(descripcion__icontains = queryset)
            ).distinct()
    return render(request, 'blog/Cat_Ayuda.html',{'post':post})

def cat_experiencia(request):
    queryset= request.GET.get("buscar")
    post=Post.objects.filter(categoria=Categoria.objects.get(nombre='Experiencia'))
    if queryset:
        post = Post.objects.filter(
                Q(titulo__icontains = queryset) | 
                Q(descripcion__icontains = queryset)
            ).distinct()
    return render(request, 'blog/Cat_Experiencia.html',{'post':post})

def cat_noticia(request):
    queryset= request.GET.get("buscar")
    post=Post.objects.filter(categoria=Categoria.objects.get(nombre='Noticia'))
    if queryset:
        post = Post.objects.filter(
                Q(titulo__icontains = queryset) | 
                Q(descripcion__icontains = queryset)
            ).distinct()
    return render(request, 'blog/Cat_Noticia.html',{'post':post})

def cat_consultas(request):
    queryset= request.GET.get("buscar")
    post=Post.objects.filter(categoria=Categoria.objects.get(nombre='Consultas'))
    if queryset:
        post = Post.objects.filter(
                Q(titulo__icontains = queryset) | 
                Q(descripcion__icontains = queryset)
            ).distinct()
    return render(request, 'blog/Cat_Consultas.html',{'post':post})

def informacion(request):
    return render(request, 'blog/informacion.html')

def detallePost(request,slug):
    if slug:
        queryset= request.GET.get("buscar")
        post = get_object_or_404(Post,slug = slug) #Si encuentra el objeto que lo traiga, sino muestra un 404 error como resultado
        if queryset:
            post = Post.objects.filter(
                    Q(titulo__icontains = queryset) | 
                    Q(descripcion__icontains = queryset)
                ).distinct()
        return render(request,'blog/post.html',{'detallePost':post})
    else:
        return render(request, 'blog/index.html',{'post':post})

def crearAutor(request):
    if request.method == 'POST': #Para registrarse
        autor_form = AutorForm(request.POST)
        if autor_form .is_valid():
            autor_form.save()
            return redirect('blog') #En index debe ir el template que permita crear post, desloguarte, etc.
    else:
        autor_form = AutorForm()
    return render(request, 'blog/registrarvista.html',{'autor_form':autor_form})
# Create your views here.

class home(ListView):
    model = EnableCenter
    template_name = 'home.html'
    context_object_name = 'lugares'


def quienes_somos(request):
    return render(request, 'quienes_somos.html')


@login_required(login_url='login')
def agregar_comentario(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detallePost', slug=post.slug)
    else:
        form = ComentarioForm()
    return render(request, 'blog/agregar_comentario.html', {'form': form})

@login_required(login_url='login')
def aprobar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.approve()
    #return redirect('detalle', pk=comentario.post.pk)
    #return redirect('detallePost', slug=post.slug)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'detalle/'))

@login_required(login_url='login')
def borrar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()
    #return redirect('detallePost', pk=comentario.post.pk)
    #return redirect('detallePost', slug=post.slug)
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'detalle/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'detalle/'))
