from django.urls import path
from . import views
urlpatterns = [

    path('recommend/', views.get_similar_recommendation, name='recommend'),
]