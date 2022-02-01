from rest_framework import serializers
from .models import Movie_Collected


class Movie_Collected_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Collected
        fields = '__all__'

