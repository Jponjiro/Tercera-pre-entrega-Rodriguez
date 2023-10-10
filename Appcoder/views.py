from django.shortcuts import render
from .models import Autor, Libro, Ejemplar
from .forms import AutorForm, LibroForm, EjemplarForm

def formulario_insertar(request):
    autor_form = AutorForm()
    libro_form = LibroForm()
    ejemplar_form = EjemplarForm()

    if request.method == 'POST':
        if 'autor' in request.POST:
            autor_form = AutorForm(request.POST)
            if autor_form.is_valid():
                autor_form.save()

        if 'libro' in request.POST:
            libro_form = LibroForm(request.POST)
            if libro_form.is_valid():
                libro_form.save()

        if 'ejemplar' in request.POST:
            ejemplar_form = EjemplarForm(request.POST)
            if ejemplar_form.is_valid():
                ejemplar_form.save()

    return render(request, 'insertar.html', {'autor_form': autor_form, 'libro_form': libro_form, 'ejemplar_form': ejemplar_form})

def buscar(request):
    if request.method == 'POST':
        termino_busqueda = request.POST.get('busqueda', '')
        resultados = Libro.objects.filter(titulo__icontains=termino_busqueda)

    return render(request, 'buscar.html', {'resultados': resultados})

