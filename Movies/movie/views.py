
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Movies.movie.models import Movie, Genre, Actor
from Movies.movie.serializers import MovieListSerializer, MovieDetailSerializer, MovieDeleteUpdateCreateSerializer, \
    NestedGenreSerializer, NestedActorsSerializer


class MovieViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieDetailSerializer
        return MovieDeleteUpdateCreateSerializer

    def get_queryset(self):
        queryset = Movie.objects.all().order_by('id')

        return queryset

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny(), ]
        return [IsAuthenticated(), ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.soft_delete()


class GenreListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = NestedGenreSerializer
    permission_classes = (
        AllowAny,
    )


class ActorsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Actor.objects.all()
    serializer_class = NestedActorsSerializer
    permission_classes = (
        AllowAny,
    )

