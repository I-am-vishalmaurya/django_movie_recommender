from rest_framework import serializers
from movies.models import Movie_Collected




class Top10MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imdb_id = serializers.CharField(max_length=100)
    original_title = serializers.CharField()
    poster_path = serializers.CharField()
    vote_average = serializers.FloatField()
    vote_count = serializers.IntegerField()
    ratings = serializers.SerializerMethodField(
        method_name="get_ratings"
    )

    def get_ratings(self, movie: Movie_Collected):
        return movie.vote_count / movie.vote_average

