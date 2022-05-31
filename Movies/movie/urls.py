from django.urls import path, include
from rest_framework import routers

from Movies.movie.views import MovieViewSet, GenreListViewSet, ActorsListViewSet, RatingCreateViewSet

router = routers.DefaultRouter()

router.register('movies', MovieViewSet, 'movies')
router.register('genre', GenreListViewSet, 'genre')
router.register('actors', ActorsListViewSet, 'actors')
router.register('rating', RatingCreateViewSet, 'rating')


urlpatterns = (
    path('', include(router.urls)),
)
