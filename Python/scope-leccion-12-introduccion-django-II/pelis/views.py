from django.shortcuts import render

# Create your views here.
from .models import Director, Genre, Movie


def index(request):
    """
        Me estoy conectando con la base de datos y extrayendo la siguiente informacion:
            - num_movies: Cuenta la cantidad de registros en el modelo Movie
            - num_genre: Cuenta la cantidad de registros en el modelo Genre
            - num_directors: Cuenta la cantidad de registros en el modelo Directors

        Otras funciones:
            - Model.objects.filter().count()

    --    --    --    --    --    --
    return render(
        request,: va por default
        template: cual es el archivo html que renderiza
        context: valores que va a recibir el archivo html desde python
    )
    """
    all_movies = Movie.objects.all()
    all_genre = Genre.objects.all()
    all_directors = Director.objects.all()

    num_movies = Movie.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_directors = Director.objects.all().count()

    return render(
        request,
        "index.html",
        context={
            "all_movies": all_movies,
            "all_genre": all_genre,
            "all_directors": all_directors,
            "num_movies": num_movies,
            "num_genre": num_genre,
            "num_directors": num_directors,
        },
    )
