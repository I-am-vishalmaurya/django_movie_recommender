from user_movies.models import MovieComments
from .models import Movie_Collected, MovieRatings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Movie_Collected_Serializer, MovieRatingSerializer


# Create your views here.

@api_view(['GET'])
def top_10(request):
    """
    This function returns the top 10 movies from the database.
    :param request:
    :return:
    """
    if request.method == 'GET':
        movie_ratings = Movie_Collected.objects.all().order_by('-vote_count')[:10]
        serializer = Movie_Collected_Serializer(movie_ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def movies(request, movie_id):
    if request.method == 'GET':
        if movie_id is not None:
            if Movie_Collected.objects.filter(id=movie_id).exists():
                serializer = Movie_Collected_Serializer(Movie_Collected.objects.get(id=movie_id))
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                content = {'message': 'No movie with this id'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        content = {'message': 'Method not allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def search_movie(request, movie_title):
    if request.method == 'GET':
        if movie_title is not None:
            collected = Movie_Collected.objects.filter(original_title__icontains=movie_title)
            if collected.exists():
                serializer = Movie_Collected_Serializer(collected, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                content = {'message': 'No movie with this title'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def add_comments(request, movie_id):
    if request.method == 'GET':
        if movie_id is not None:
            comment = request.data.get('comment')
            movie = Movie_Collected.objects.get(pk=movie_id)
            if comment is not None:
                MovieComments.objects.create(user=request.user, movie=movie, comment=comment)
                context = {
                    'movie': movie.original_title,
                    'comment': comment
                }
                return Response(data=context, status=status.HTTP_200_OK)
            else:
                message = {"error": "Comment field is empty"}
                return Response(data=message, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_rating(request, movie_id):
    # global review, rating
    if request.method == 'POST':
        if movie_id is not None:
            try:
                if 'rating' in request.data or 'review' in request.data:
                    movie = Movie_Collected.objects.get(pk=movie_id)
                    if 'rating' in request.data:
                        rating = request.data.get('rating')
                        if 'review' in request.data:
                            review = request.data.get('review')
                        else:
                            review = None
                    else:
                        rating = None

                    movie_rating_object = MovieRatings.objects.filter(user=request.user, movie=movie).exists()
                    if movie_rating_object:
                        MovieRatings.objects.filter(user=request.user, movie=movie).update(rating=rating, review=review)
                        return Response(status=status.HTTP_200_OK)
                    else:
                        MovieRatings.objects.create(user=request.user, movie_id=movie.id, rating=rating, review=review)
                        to_update = Movie_Collected.objects.filter(pk=movie_id)
                        to_update.update(
                            # Increase vote average and vote count
                            vote_average=round(
                                (to_update.get().vote_average * to_update.get().vote_count + request.data.get(
                                    'rating')) / (to_update.get().vote_count + 1), 2),
                            vote_count=to_update.get().vote_count + 1
                        )
                        return Response(status=status.HTTP_200_OK)

                else:
                    message = {"error": "Rating field is missing"}
                    return Response(data=message, status=status.HTTP_406_NOT_ACCEPTABLE)
            except Movie_Collected.DoesNotExist:
                message = {"error": "Movie does not exist"}
                return Response(data=message, status=status.HTTP_404_NOT_FOUND)
        else:
            message = {"error": "Movie id is empty"}
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUserRatedMovies(request, movie_id):
    if request.method == 'GET':
        user_ratings = MovieRatings.objects.filter(user_id=request.user.id, movie_id=movie_id)
        if user_ratings.exists():
            ratings = MovieRatings.objects.get(user_id=request.user.id, movie_id=movie_id)
            serializer = MovieRatingSerializer(ratings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {"error": "User has no ratings"}
            return Response(data=message, status=status.HTTP_404_NOT_FOUND)
