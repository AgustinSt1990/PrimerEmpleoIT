from django.db import models
from django.urls import reverse


class Genre(models.Model):
    genre = models.CharField(max_length=64)

    def __str__(self):
        return self.genre


class Movie(models.Model):
    title = models.CharField(
        max_length=64, help_text="Ingresa el nombre de la Pelicula"
    )
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    summary = models.TextField(
        max_length=100, help_text="Escribe la descripcion de la Pelicula", null=True
    )
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie-detail", args=[str(self.id)])


class Director(models.Model):
    last_name = models.CharField(
        max_length=64, help_text="Ingrese el apellido del director"
    )
    first_name = models.CharField(
        max_length=64, blank=True, null=True, help_text="Ingrese el nombre del director"
    )
    # movies = models.ManyToManyField(Movie)

    def __str__(self):
        if self.first_name == "" or self.first_name == None:
            return self.last_name
        else:
            return self.first_name + " " + self.last_name
