from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies.models import MovieRatings, Movie_Collected
from .serializers import MovieSerializer
from movies.serializers import Movie_Collected_Serializer
import pandas as pd
import pickle
import warnings

warnings.filterwarnings("ignore")

cosine_sim = pickle.load(open('management/working/similarity.pkl', 'rb'))
df = pd.DataFrame(list(Movie_Collected.objects.all().values()))
df = df.reset_index()
titles = df['original_title']
indices = pd.Series(df.index, index=titles)


def improved_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:25]
    movie_indices = [i[0] for i in sim_scores]

    movies = df.loc[movie_indices][['id', 'original_title', 'vote_count', 'vote_average', 'year']]
    vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(0.60)
    qualified = movies[
        (movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    #     qualified['wr'] = qualified.apply(weighted_rating, axis=1)
    qualified = qualified.sort_values('vote_count', ascending=False).head(10)
    return qualified


@api_view(['POST'])
def get_similar_recommendation(request):
    """
    This function returns the similar movies from db
    :param movie:
    :param request:
    :return:
    """
    if request.method == 'POST':
        movie = request.data['movie']
        similar_movies = improved_recommendations(movie).id.values
        similar_movies = Movie_Collected.objects.filter(id__in=similar_movies)
        serializer = Movie_Collected_Serializer(similar_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
