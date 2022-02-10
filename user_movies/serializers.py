from rest_framework import serializers, fields
from user_movies.models import WatchList


class MovieDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    original_title = serializers.CharField(max_length=255)
    vote_average = serializers.FloatField()
    vote_count = serializers.IntegerField()
    original_language = serializers.CharField(max_length=1000)
    overview = serializers.CharField()
    genres = serializers.CharField()
    runtime = serializers.IntegerField()
    poster_path = serializers.CharField()


class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    movie = MovieDetailSerializer()

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.save()
        return instance

