"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
# from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.models import User
from streaming import views

# from streaming import views_api as api_views

app_name = 'streaming'
urlpatterns = [
    path('', views.home, name='home'),
    # path('crud/', views.crud, name='crud'),
    # path('crud/<str:model_type>/', views.crud, name='crud'),
    # path('crud/<str:model_type>/<int:entry_id>/', views.crud, name='crud'),
    # path('api/', include('streaming.urls_api', namespace='api')),
    path('api/', views.api_main, name='api_main'),
    path('api/index/', include('streaming.urls_api')),
    path('api/crud/', views.api_crud, name='api_crud'),

    path('genres/', views.genres, name='genre_categories'),
    path('genres/<str:genre_pk>/', views.genre_list, name='genre_list'),
    path('genres/<str:video_type>/<int:genre_pk>/', views.genre_list, name='genre_list_type'),

    # TODO: Change 'tv_list' to 'show_list'
    path('shows/', views.tv_list, name='tv_list'),
    # path('video/', views.video_detail, name='video_detail'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('video/<str:video_type>/<int:video_pk>/', views.video_detail_type, name='video_detail_type'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    # Movie URLs
    path('movies/', views.movie_list, name='movie_list'),
    # path('movies/create/', views.create_movie, name='movie_create'),
    path('movies/<int:pk>/edit/', views.update_movie, name='movie_update'),
    path('movies/<int:pk>/delete/', views.delete_movie, name='movie_delete'),

    # Actor URLs
    # path('actors/', views.actor_lisT, name='actor_list'),
    # path('actors/create/', views.actor_create_view, name='actor_create'),
    path('actors/<int:pk>/edit/', views.update_actor, name='actor_update'),
    path('actors/<int:pk>/delete/', views.delete_actor, name='actor_delete'),
]
