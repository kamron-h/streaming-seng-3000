# views_api.py

from rest_framework import viewsets
from .models import Movie, Actor, Rating, Show, Genre
from .serializers import MovieSerializer, ActorSerializer, RatingSerializer, \
    ShowSerializer, GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# Create RatingViewSet here
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


# Create ShowViewSet here
class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


# Create GenreViewSet here
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
