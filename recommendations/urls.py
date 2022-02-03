from django.urls import path
from . import views
urlpatterns = [
    path('top/', views.top_10, name='top10'),
    path('recommend/', views.get_similar_recommendation, name='recommend'),
]