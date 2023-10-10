from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Ejemplar(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.libro.titulo} - {self.estado}'
