from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import FloatField, Avg
from django.db.models.functions import Coalesce

from Movies.soft_delete_app.models import SoftDeleteModel

UserModel = get_user_model()


class Genre(models.Model):
    NAME_MAX_LENGTH = 30

    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return f'{self.name}'


class Actor(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(SoftDeleteModel):
    MOVIE_NAME_MAX_LENGTH = 30

    name = models.CharField(
        max_length=MOVIE_NAME_MAX_LENGTH,
        unique=True,
    )

    date = models.DateField()

    actors = models.ManyToManyField(
        Actor,
    )

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    poster = models.URLField()

    trailer = models.URLField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def average_rating(self):
        ratings = Rating.objects.filter(movie=self).aggregate(average=Avg('vote'))
        avg = 0
        if ratings['average'] is not None:
            avg = float(ratings['average'])
        return avg

    def __str__(self):
        return f'{self.name}'


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    vote = models.PositiveIntegerField(
        validators=(MaxValueValidator(5),)
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
