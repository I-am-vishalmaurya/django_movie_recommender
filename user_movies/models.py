from django.db import models
from movies.models import Movie_Collected
# Custom Settings
from django.conf import settings
# Create your models here.


class LikedMovies(models.Model):
    movie = models.ForeignKey(Movie_Collected, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)


class WatchedMovies(models.Model):
    movie = models.ForeignKey(Movie_Collected, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)


class WatchList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_Collected, on_delete=models.CASCADE)


class MovieComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_Collected, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)

