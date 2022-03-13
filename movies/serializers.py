from rest_framework import serializers
from .models import Movie_Collected
from .models import MovieRatings


class Movie_Collected_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Collected
        fields = '__all__'


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = '__all__'
