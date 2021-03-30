from rest_framework.response import Response
from netflix.models import Movie
from .serializers import MovieSerializer, MovieSerializerCreate
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import  viewsets
from rest_framework.decorators import api_view, permission_classes



@api_view(["GET",])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)



@api_view(["POST",])
#@permission_classes([IsAuthenticated,])
def create(request):
    serializer = MovieSerializerCreate(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success" : True,
            "message": "Movie has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success" : False,
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


class UpdateMovie(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [IsAuthenticated]

class DeleteMovie(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [IsAuthenticated]