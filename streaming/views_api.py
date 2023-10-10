# views_api.py

from rest_framework import viewsets
from .models import Video, Actor, Rating
from .serializers import VideoSerializer, ActorSerializer, RatingSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# Create RatingViewSet here
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
