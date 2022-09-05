# Generated by Django 4.0.6 on 2022-09-03 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Ingrese el apellido del director", max_length=64
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        help_text="Ingrese el nombre del director",
                        max_length=64,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genre", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Ingresa el nombre de la Pelicula", max_length=64
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "summary",
                    models.TextField(
                        help_text="Escribe la descripcion de la Pelicula",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "director",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pelis.director",
                    ),
                ),
                ("genre", models.ManyToManyField(to="pelis.genre")),
            ],
        ),
    ]