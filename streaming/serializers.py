# serializers.py

from rest_framework import serializers
from .models import Movie, Actor, Rating, \
    Show, Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
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


# Serializer for Show model
class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'  # use all fields from the Show model


# Serializer for Genre model
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'  # use all fields from the Genre model
