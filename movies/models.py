from django.conf import settings
from django.db import models


# Create your models here.


class Movie_Collected(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    tmdb_id = models.IntegerField(null=True, unique=True)
    original_title = models.CharField(max_length=1000, null=False)
    original_language = models.CharField(max_length=1000, null=True)
    overview = models.TextField(null=True)
    genres = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.CharField(max_length=1000, null=True)
    production_company= models.CharField(max_length=1000, null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    revenue = models.BigIntegerField(null=True)
    year = models.IntegerField(null=True)
    adult = models.BooleanField(null=True)
    budget = models.BigIntegerField(null=True)
    spoken_languages = models.TextField(null=True)
    status = models.CharField(max_length=1000, null=True)
    runtime = models.IntegerField(null=True)

    def __str__(self):
        return self.original_title, self.original_language, self.overview, self.popularity, self.vote_average, \
               self.vote_count, self.revenue, self.adult, self.budget


class Movie_Details(models.Model):
    tmdb_id = models.IntegerField(null=True, unique=True)
    cast = models.TextField(null=True)
    crew = models.TextField(null=True)
    director = models.CharField(max_length=1000, null=True)
    soup = models.TextField(null=True)


class MovieRatings(models.Model):
    movie = models.ForeignKey(Movie_Collected, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    review = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
