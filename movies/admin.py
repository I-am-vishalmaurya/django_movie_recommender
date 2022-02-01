from django.contrib import admin
from .models import Movie_Collected
# Register your models here.


class Movie_Collected_Admin(admin.ModelAdmin):
    list_display = ('original_title', 'original_language', 'popularity', 'vote_count', 'vote_average')
    search_fields = ['original_title']
    list_per_page = 30


admin.site.register(Movie_Collected, Movie_Collected_Admin)