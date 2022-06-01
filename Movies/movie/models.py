from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Avg


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

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


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

    # If the movie is rated, adds an average rating from all accumulated votes.
    def average_rating(self):
        ratings = Rating.objects.filter(movie=self).aggregate(average=Avg('vote'))
        avg = 0
        if ratings['average'] is not None:
            avg = str(round(float(ratings['average']), 1))
        return avg

    def __str__(self):
        return f'{self.name}'


class Rating(models.Model):
    # Separate model containing all rating records from all User
    # Not registered users can't vote
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

    class Meta:
        # Users can vote only once for every movie
        unique_together = ('user', 'movie')
