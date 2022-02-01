from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie_Details, Movie_Collected
from .serializers import Top10MovieSerializer
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
from django.db import connection

# Create your views here.

# query = str(Movie_Collected.objects.all().query)
# df = pd.read_sql_query(query, con=connection)
# count_vectorizer = CountVectorizer(stop_words="english")
# count_matrix = count_vectorizer.fit_transform(df['original_title'])
# cosine_sim = cosine_similarity(count_matrix)


# def get_recommendation(movie_id):
#     """
#     This function returns the top 10 movies from the database.
#     :param movie_id:
#     :return:
#     """
#     movie_index = df[df['id'] == movie_id].index[0]
#     similar_movies = list(enumerate(cosine_sim[movie_index]))
#     sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
#     sorted_similar_movies = sorted_similar_movies[1:11]
#     movie_indices = [i[0] for i in sorted_similar_movies]
#     # return title of the movies
#     print(df['original_title'].iloc[movie_indices])
#     return df['original_title'].iloc[movie_indices]



#
# def get_recommendation_using_title(title, cosine_sim=coisine_sim):

@csrf_exempt
@api_view(['POST'])
def top_10(request):
    """
    This function returns the top 10 movies from the database.
    :param request:
    :return:
    """
    # ans = get_recommendation(22509)
    if request.method == 'POST':
        movie_ratings = Movie_Collected.objects.all().order_by('-vote_count')[:10]
        serializer = Top10MovieSerializer(movie_ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
