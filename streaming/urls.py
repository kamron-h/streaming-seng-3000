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
from streaming import views
# from streaming import views_api as api_views

app_name = 'streaming'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.api_index, name='api_index'),
    # path('crud/', views.crud, name='crud'),
    # path('crud/<str:model_type>/', views.crud, name='crud'),
    # path('crud/<str:model_type>/<int:entry_id>/', views.crud, name='crud'),
    # path('api/', include('streaming.urls_api', namespace='api')),
    path('api/', views.api_main, name='api_main'),
    path('api/crud/', views.crud, name='crud'),

    path('genres/', views.genres, name='genre_list'),
    path('movies/', views.movie_list, name='movie_list'),
    path('shows/', views.tv_list, name='tv_list'),
    path('video/', views.video_detail, name='video_detail'),
    # path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
