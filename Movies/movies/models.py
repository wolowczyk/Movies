from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=81)
    nationality = models.CharField(max_length=81)


class Movie(models.Model):
    title = models.CharField(max_length=81)
    description = models.TextField(default="opis")
    director = models.ForeignKey(Person)
    year = models.IntegerField()
    actors = models.ManyToManyField(Person, through='Role', related_name='playing')


class Role(models.Model):
    character = models.CharField(max_length=81)
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Person)
