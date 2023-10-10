from django import forms
from .models import Autor, Libro, Ejemplar

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class EjemplarForm(forms.ModelForm):
    class Meta:
        model = Ejemplar
        fields = '__all__'
