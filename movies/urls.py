from django.urls import path
from . import views

urlpatterns = [
    path('get_movie/<int:movie_id>', views.movies, name='movies'),
    path('search_movies/<str:movie_title>', views.search_movie, name='search_movie'),
    path('add_comments/<int:movie_id>', views.add_comments, name='add_comments'),
    path('rate_movie/<int:movie_id>', views.create_rating, name='rate_movie'),
    path('top/', views.top_10, name='top10'),
]
