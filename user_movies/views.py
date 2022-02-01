from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie_Collected
from .models import  WatchList, MovieComments
from .serializers import WatchListSerializer


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def watch_list(request):
    """
    Get watchlist or create a watchlist, or delete from watchlist
    :param request:
    :return:
    """
    if request.method == 'GET':
        watchlist = WatchList.objects.filter(user=request.user)
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        movie_id = request.data.get('movie_id')
        if movie_id is not None:
            # check if movie is in db
            try:
                movie = Movie_Collected.objects.get(pk=movie_id)
                watchlist = WatchList.objects.filter(user=request.user, movie=movie).exists()
                if watchlist:
                    message = {"error": "Movie already in watchlist"}
                    return Response(data=message, status=status.HTTP_400_BAD_REQUEST)
                else:
                    watchlist = WatchList.objects.create(user=request.user, movie=movie)
                    serializer = WatchListSerializer(watchlist)
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            except Movie_Collected.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            message = {'error': 'Movie id is required'}
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie_id = request.data.get('movie_id')
        if movie_id is not None:
            try:
                movie = Movie_Collected.objects.get(pk=movie_id)
                WatchList.objects.filter(user=request.user, movie=movie).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Movie_Collected.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            message = {'error': 'Movie id is required'}
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)


