from django.contrib import admin
from django.contrib.admin import ModelAdmin

from Movies.movie.models import Actor, Genre, Movie, Rating


@admin.register(Actor)
class CustomUserAdmin(ModelAdmin):
    pass


@admin.register(Genre)
class CustomUserAdmin(ModelAdmin):
    list_display = ['name']


@admin.register(Movie)
class CustomUserAdmin(ModelAdmin):
    pass


@admin.register(Rating)
class CustomUserAdmin(ModelAdmin):
    list_display = ['movie', 'vote', 'user']
