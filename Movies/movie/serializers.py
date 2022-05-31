from django.contrib.auth import get_user_model
from rest_framework import serializers

from Movies.movie.models import Movie, Actor, Genre, Rating

UserModel = get_user_model()


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username')


class NestedGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class NestedActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'last_name')


class RatingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        rating_instance = Rating.objects.create(**validated_data)

        return rating_instance

    class Meta:
        model = Rating
        fields = ('vote', 'movie')


class MovieListSerializer(serializers.ModelSerializer):
    actors = NestedActorsSerializer(many=True, )
    genre = NestedGenreSerializer(many=False, )

    class Meta:
        model = Movie
        fields = ('id', 'name', 'actors', 'genre', 'poster')


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = NestedActorsSerializer(many=True, )
    genre = NestedGenreSerializer(many=False, )
    user = NestedUserSerializer(many=False, )

    is_rated = serializers.SerializerMethodField()

    def get_is_rated(self, obj):
        request_user = self.context['request'].user
        return Rating.objects.filter(movie=obj, user=request_user).exists()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'actors', 'genre', 'poster', 'trailer', 'user', 'average_rating', 'date', 'is_rated')


class MovieDeleteUpdateCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        actors = validated_data.pop('actors')
        movie_instance = Movie.objects.create(**validated_data)
        for actor in actors:
            movie_instance.actors.add(actor)

        return movie_instance

    class Meta:
        model = Movie
        fields = ('name', 'date', 'actors', 'genre', 'poster', 'trailer')
