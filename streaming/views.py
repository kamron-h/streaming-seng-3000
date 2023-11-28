from random import random

from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Movie, Actor
from .forms import MovieForm, ActorForm

CRUD_URL = 'streaming/api_crud.html'
CRUD_URL_REDIRECT = 'streaming:api_crud'
# GET_ACTOR_OBJ_404 = get_object_or_404(Actor, pk=pk)


def create_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key


def get_user_token(user):
    token = Token.objects.get(user=user)
    return token.key


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


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect(CRUD_URL_REDIRECT)


# Create a function to handle update_movie requests
def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    instance = get_object_or_404(Movie, pk=pk) if pk else None

    if request.method == 'POST':
        # Create a movie form instance with the submitted data and the movie instance
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if not instance:
            return HttpResponse("Invalid request. No ID provided for update.", status=400)
        if form.is_valid():
            form.save()
            return redirect(CRUD_URL_REDIRECT)  # Redirect to a success URL
        # Handle form errors in context below
    else:
        # Create a form instance for GET request to display the existing movie data
        form = MovieForm(instance=movie)

    return render(request, 'streaming/api/update_movie.html', {'form': form, 'movie': movie})


def delete_actor(request, pk):
    movie = get_object_or_404(Actor, pk=pk)
    movie.delete()
    return redirect(CRUD_URL_REDIRECT)


# Create a function to handle update_movie requests
def update_actor(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    instance = get_object_or_404(Actor, pk=pk) if pk else None

    if request.method == 'POST':
        # Create a movie form instance with the submitted data and the movie instance
        form = ActorForm(request.POST, request.FILES, instance=actor)
        if not instance:
            return HttpResponse("Invalid request. No ID provided for update.", status=400)
        if form.is_valid():
            form.save()
            return redirect(CRUD_URL_REDIRECT)  # Redirect to a success URL
        # Handle form errors in context below
    else:
        # Create a form instance for GET request to display the existing movie data
        form = ActorForm(instance=actor)

    return render(request, 'streaming/api/update_actor.html', {'form': form, 'actor': actor})


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
@login_required(login_url='members:login')
def api_crud(request, entry_id=None):
    movies = Movie.objects.all().order_by('uploaded_at')
    actors = Actor.objects.all().order_by('created_at')
    mov_paginate = Paginator(movies, 6 if movies.count() > 6 else movies.count())
    act_paginate = Paginator(actors, 6 if actors.count() > 6 else actors.count())

    movieInstance = get_object_or_404(Movie) if entry_id else None
    actorInstance = get_object_or_404(Actor) if entry_id else None

    token = Token.objects.get(user=request.user)

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        actor_form = ActorForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
            return redirect(CRUD_URL)  # Redirect to a success URL
        # Handle form errors in context below
        if actor_form.is_valid():
            actor_form.save()
            return redirect(CRUD_URL)  # Redirect to a success URL
        # Handle form errors in context below

    elif request.method == 'DELETE':
        if not movieInstance:
            return HttpResponse("Invalid request. No ID provided for deletion.", status=400)
        movieInstance.delete()
        if not actorInstance:
            return HttpResponse("Invalid request. No ID provided for deletion.", status=400)
        actorInstance.delete()
        return redirect(CRUD_URL)

    else:  # GET request
        movie_form = MovieForm(instance=movieInstance)
        actor_form = ActorForm(instance=actorInstance)

    context = {
        'movie_form': movie_form,
        'actor_form': actor_form,
        'movies': mov_paginate.get_page(request.GET.get('page', 1)),
        'actors': act_paginate.get_page(request.GET.get('page', 1)),
        'entry_id': entry_id,
        'token': token.key,
        # 'Authorization': f' Auth',
    }

    return render(request, CRUD_URL, context)


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
