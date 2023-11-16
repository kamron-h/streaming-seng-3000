from random import random

from django.contrib.sites import requests
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from streaming.forms import MovieForm, ActorForm
from streaming.models import Actor, Movie, Show, Genre

# JWT-REST authentication
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status

CRUD_URL = 'streaming/api_crud.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'streaming/signup.html', {'form': form})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_crud(request, model_type=None, entry_id=None):
    ModelForm = MovieForm if model_type == "movies" else ActorForm
    Model = Movie if model_type == "movies" else Actor
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    mov_paginate = Paginator(movies, 6)
    act_paginate = Paginator(actors, 6)

    instance = None
    if entry_id:
        instance = get_object_or_404(Model, id=entry_id)

    if request.method == 'GET':
        form = ModelForm(instance=instance)
        context = {
            'form': form,
            'movies': movies,
            'actors': actors,
            'entry_id': entry_id,
            'mov_paginate': mov_paginate,
            'act_paginate': act_paginate,
        }
        return render(request, CRUD_URL, context)

    # For POST, PUT, DELETE, handle as API
    elif request.method in ['POST', 'PUT']:
        form = ModelForm(request.data, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            message = 'Item created successfully' if request.method == 'POST' else 'Item updated successfully'
            return Response({'message': message}, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not instance:
            return Response({'error': 'Invalid request. No ID provided for deletion.'}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


def api_index(request):
    return render(request, 'streaming/api_index.html')


def home(request):
    movies = Movie.objects.all()[:12]  # [:20] Used to limit
    shows = Show.objects.all()[:12]  # [:20] Used to limit
    cover_movs = Movie.objects.exclude(cover_url__isnull=True)[:5]  # Movies used in the carousel
    latest_shows = shows[:6]
    latest_movs = movies[:6]
    # Sort latest_movies in ascending
    # mov_paginate = Paginator(movies, 6)
    # show_paginate = Paginator(movies, 6)
    context = {
        'movies': movies,
        'shows': shows,
        'cover_movs': cover_movs,
        'latest_shows': latest_shows,
        'latest_movs': latest_movs,
        # 'mov_paginate': mov_paginate,
        # 'show_paginate': show_paginate,
    }
    return render(request, 'streaming/home.html', context)


def api_main(request):
    return render(request, 'streaming/api_main.html')


# def crud(request):
#     return render(request, 'streaming/crud.html')


def crud(request):
    movies = Movie.objects.all()[:2]
    actors = Actor.objects.all()[:3]
    return render(request, 'streaming/api_crud.html', {'movies': movies, actors: 'actors'})


def movie_list(request):
    movies = Movie.objects.all()[:12]  # [:20] Used to limit
    cover_movies = Movie.objects.exclude(cover_url__isnull=True)[:5]  # Movies used in the carousel
    # Sort latest_movies in ascending
    if movies.count() > 18:
        movie_paginate = Paginator(movies, 18)
        context = {
            'movies': movies,
            'cover_movies': cover_movies,
            'movie_paginate': movie_paginate
        }
    else:
        context = {
            'movies': movies,
            'cover_movies': cover_movies,
        }

    return render(request, 'streaming/movie_list.html', context)


def tv_list(request):
    shows = Show.objects.all()[:12]  # [:20] Used to limit
    cover_shows = Show.objects.exclude(cover_url__isnull=True)[:5]  # Movies used in the carousel
    # Sort latest_movies in ascending
    if shows.count() > 18:
        show_paginate = Paginator(shows, 18)
        context = {
            'shows': shows,
            'cover_shows': cover_shows,
            'show_paginate': show_paginate
        }
    else:
        context = {
            'shows': shows,
            'cover_shows': cover_shows,
        }

    return render(request, 'streaming/tv_list.html', context)


def genres(request):
    genres_ls = Genre.objects.all()
    return render(request, 'streaming/genres.html', {'genres_ls': genres_ls})


def genre_list(request, video_type=None, genre_pk=None):
    genre = get_object_or_404(Genre, pk=genre_pk)
    context = {}
    if video_type == "Movie":
        # Get all the movies with the given genre pk
        # Sort latest_movies in ascending order based on premiere_date where movie.thumbnail_url is not null
        # Place the sorted movies in a list called 'movie_recs'
        movies = Movie.objects.filter(genres__pk=genre_pk)
        movie_recs = Movie.objects.filter(genres__pk=genre_pk, cover_url__isnull=False).random_order()
        context = {
            'genre': genre,
            'videos': movies,
            'video_recs': movie_recs
        }
    elif video_type == "Show":
        # Get all the shows with the given genre pk
        # Sort latest_shows in ascending order based on premiere_date where show.thumbnail_url is not null
        # Place the sorted shows in a list called 'show_recs'
        shows = Show.objects.filter(genres__pk=genre_pk)
        show_recs = Show.objects.filter(genres__pk=genre_pk, cover_url__isnull=False).order_by('premiere_date')
        context = {
            'genre': genre,
            'videos': shows,
            'video_recs': show_recs
        }
    elif video_type != "Movie" and video_type != "Show":
        # Get all the shows with the given genre pk Sort latest_movies & latest_shows in ascending order based on
        # premiere_date where movie.thumbnail_url & show.thumbnail_url are not individually null. Place the sorted
        # movies & shows combined in one list called 'video_recs'
        movies = Movie.objects.filter(genres__pk=genre_pk)
        shows = Show.objects.filter(genres__pk=genre_pk)
        movie_recs = Movie.objects.filter(genres__pk=genre_pk, cover_url__isnull=False).order_by('premiere_date')
        show_recs = Show.objects.filter(genres__pk=genre_pk, cover_url__isnull=False).order_by('premiere_date')
        videos = list(movies) + list(shows)
        video_recs = list(movie_recs) + list(show_recs)

        # random.shuffle(videos)
        context = {
            'genre': genre,
            'videos': videos,
            'video_recs': video_recs
        }
    return render(request, 'streaming/genre_list.html', context)


def video_detail(request, video_id=None):
    video = get_object_or_404(Movie, pk=video_id)
    # Sort latest_movies in ascending order based on premiere_date
    latest_shows = Show.objects.all().order_by('premiere_date')  # [:6] Used to limit
    return render(request, 'streaming/video_detail.html',
                  {'video': video, 'latest_movies': latest_shows})


def video_detail_type(request, video_type, video_pk):
    if video_type == "Movie":
        video = (get_object_or_404(Movie, pk=video_pk))
        # Sort latest_movies in ascending order based on premiere_date
        video_recs = Movie.objects.all().order_by('premiere_date')[:6]
    else:
        video = (get_object_or_404(Show, pk=video_pk))
        # Sort latest_movies in ascending order based on premiere_date
        video_recs = Show.objects.all().order_by('premiere_date')[:6]  # [:6] Used to limit
    return render(request, 'streaming/video_detail.html',
                  {'video': video, 'video_recs': video_recs})


# def video_detail(request, video_id):
#     video = get_object_or_404(Video, pk=video_id)
#     return render(request, 'streaming/video_detail.html', {'video': video})


def privacy_policy(request):
    return render(request, 'streaming/privacy_p.html')
