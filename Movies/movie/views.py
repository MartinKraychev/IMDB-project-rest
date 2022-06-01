from rest_framework import viewsets, status, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Movies.movie.models import Movie, Genre, Actor, Rating
from Movies.movie.permissions import IsOwnerOfObject
from Movies.movie.serializers import MovieListSerializer, MovieDetailSerializer, MovieDeleteUpdateCreateSerializer, \
    NestedGenreSerializer, NestedActorsSerializer, RatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    filterset_fields = ('name', 'genre__name', 'actors__first_name', 'actors__last_name', 'user__username')

    # Uses a different serializers depending on action
    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieDetailSerializer
        return MovieDeleteUpdateCreateSerializer

    def get_queryset(self):
        queryset = Movie.objects.all().order_by('id')

        return queryset

    # Different permissions depending on action
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny(), ]
        elif self.action == 'update' or self.action == 'destroy':
            # Edit or delete checks if user is owner first, returns 403 if not.
            return [IsAuthenticated(), IsOwnerOfObject(), ]
        return [IsAuthenticated(), ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Soft delete
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


class RatingCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (
        AllowAny,
    )
