# serializers.py

from rest_framework import serializers
from .models import Video, Actor, Rating


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'  # use all fields from the Video model


# Serializer for Actor model
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'  # use all fields from the Actor model


# Serializer for Rating model
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'  # use all fields from the Rating model
