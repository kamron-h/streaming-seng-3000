# urls_api.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import VideoViewSet, ActorViewSet, RatingViewSet


# Create a router and register the viewset
router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'actors', ActorViewSet, basename='actors')
router.register(r'ratings', RatingViewSet, basename='ratings')


# The API URLs are determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
