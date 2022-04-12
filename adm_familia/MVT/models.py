from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"Moive #{self.id} {self.title} ({self.genre})"


class Brand(models.Model):
    name = models.CharField(max_length=40)
    segment = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Marca #{self.id}: {self.name} ({self.segment})"


class Person(models.Model):
    name = models.CharField(max_length=30)
    born = models.DateField()
    favourite_number = models.IntegerField()
    favourite_movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    favourite_brand = models.ForeignKey(Brand, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"Persona #{self.id}: {self.name}"
