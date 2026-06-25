from rest_framework.status import HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_200_OK,HTTP_404_NOT_FOUND
from rest_framework.response import Response
from movies.serializers import MovieSerializer
from rest_framework.decorators import api_view
from movies.models import Movie

@api_view(['GET','POST'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

    
def update_movie(movie,data,partial=False):
    serializer = MovieSerializer(movie, data=data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

def delete_movie(movie):
    try:
        movie.delete()
        return Response({'message':'Movie deleted successfully'},status=HTTP_204_NO_CONTENT)
    except Movie.DoesNotExist:
        return Response({'message':'Movie not found'},status=HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','PATCH','DELETE'])
def movie_details(request,id):
    try:
        movie = Movie.objects.get(id=id)
        if request.method == 'GET':
            serializer = MovieSerializer(movie)
            return Response(serializer.data,status=HTTP_200_OK)
        elif request.method == 'PUT':
            return update_movie(movie,request.data,False)
        elif request.method == 'PATCH':
            return update_movie(movie,request.data,True)
        elif request.method == 'DELETE':
            return delete_movie(movie)
    except Movie.DoesNotExist:
        return Response({'message':'Movie not found'},status=HTTP_404_NOT_FOUND)
    

