from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from .models import Multimedia
from .forms import CursoForm
from .forms import MultimediaForm


# Create your views here.

# Acceso al sitio
def inicio(request):
    return render(request, 'paginas/inicio.html')
def contacto(request):
    return render(request, 'paginas/contacto.html')

#Acceso a los cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/index_curso.html', {'cursos': cursos})
def crear_curso(request):
    formulario = CursoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cursos')
    return render(request, 'cursos/crear_curso.html', {'formulario': formulario})
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    formulario = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cursos')
    return render(request, 'cursos/editar_curso.html', {'formulario': formulario})
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('cursos')

#Acceso a los multimedias
def multimedias(request):
    multimedias = Multimedia.objects.all()
    return render(request, 'multimedias/index_multimedias.html', {'multimedias': multimedias})
def crear_multimedias(request):
    formulariomul = MultimediaForm(request.POST or None, request.FILES or None)
    if formulariomul.is_valid():
        formulariomul.save()
        return redirect('multimedias')
    return render(request, 'multimedias/crear_multimedias.html', {'formulariomul': formulariomul})
def editar_multimedias(request,id):
    multimedia = Multimedia.objects.get(id=id)
    formulariomul = MultimediaForm(request.POST or None, request.FILES or None, instance=multimedia)
    if formulariomul.is_valid() and request.POST:
        formulariomul.save()
        return redirect('multimedias')
    return render(request, 'multimedias/editar_multimedias.html', {'formulariomul': formulariomul})
def eliminar_multimedias(request,id):
    multimedia = Multimedia.objects.get(id=id)
    multimedia.delete()
    return redirect('multimedias')   

#Index principal
def index_caro(request):
    imagen = 'img/bg-img/breadcumb.jpg'
    imagen2 = 'img/bg-img/bread.png'
    cursos = Curso.objects.all()
    multimedias = Multimedia.objects.all()
    populares = 1 # consulta ordenada por calificacion
    multimedia = 2 # consulta por clasificc+acion
    return render(request, 'index.html',{'imagen': imagen, 'imagen2': imagen2,'cursos':cursos, 'multimedias': multimedias})

   
