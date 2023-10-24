# urls_api.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import ActorViewSet, RatingViewSet, ShowViewSet, GenreViewSet, MovieViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'actors', ActorViewSet, basename='actors')
router.register(r'ratings', RatingViewSet, basename='ratings')
router.register(r'shows', ShowViewSet, basename='shows')
router.register(r'genres', GenreViewSet, basename='genres')


# The API URLs are determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
