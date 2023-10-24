from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

# Create your views here.
from streaming.forms import MovieForm, ActorForm
from streaming.models import Actor, Movie, Show

CRUD_URL = 'streaming/api_crud.html'


def api_crud(request, model_type=None, entry_id=None):
    ModelForm = MovieForm if model_type == "movies" else ActorForm
    Model = Movie if model_type == "movies" else Actor
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    mov_paginate = Paginator(movies, 6)
    act_paginate = Paginator(movies, 6)

    instance = None
    if entry_id:
        instance = get_object_or_404(Model, id=entry_id)  # Fetch the instance if entry_id is provided

    # Handle POST request (For both Video and Actor creation)
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(CRUD_URL)

    # Handle PUT request (For both Video and Actor updates)
    elif request.method == 'PUT':
        if not instance:
            return HttpResponse("Invalid request. No ID provided for update.", status=400)
        form = ModelForm(request.PUT, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(CRUD_URL)

    # Handle DELETE request (For both Video and Actor deletion)
    elif request.method == 'DELETE':
        if not instance:
            return HttpResponse("Invalid request. No ID provided for deletion.", status=400)
        instance.delete()
        return redirect(CRUD_URL)

    # Handle GET request
    else:
        form = ModelForm(instance=instance)

    context = {
        'form': form,
        'movies': movies,
        'actors': actors,
        'entry_id': entry_id,
        'mov_paginate': mov_paginate,
        'act_paginate': act_paginate,
    }

    # Render the page with the form as context
    return render(request, CRUD_URL, context)


def api_index(request):
    return render(request, 'streaming/api_index.html')


def home(request):
    movies = Movie.objects.all()[:20]
    shows = Show.objects.all()[:20]
    mov_paginate = Paginator(movies, 6)
    show_paginate = Paginator(movies, 6)
    context = {
        'movies': movies,
        'shows': shows,
        'mov_paginate': mov_paginate,
        'show_paginate': show_paginate,
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


def genres(request):
    return render(request, 'streaming/genres.html')


def movie_list(request):
    # Get or 404 the list of movies
    movies = Movie.objects.all()
    return render(request, 'streaming/movie_list.html', {'movies': movies})


def tv_list(request):
    return render(request, 'streaming/tv_list.html')


def video_detail(request, video_id=None):
    video = get_object_or_404(Movie, pk=video_id)
    # Sort latest_movies in ascending order based on premiere_date
    latest_shows = Show.objects.all().order_by('premiere_date')[:6]
    return render(request, 'streaming/video_detail.html',
                  {'video': video, 'latest_movies': latest_shows})


def video_detail_type(request, video_type=None, video_id=None):
    if video_type == "Movie":
        video = (get_object_or_404(Movie, pk=video_id))
        # Sort latest_movies in ascending order based on premiere_date
        video_recs = Movie.objects.all().order_by('premiere_date')[:6]
    #     List another word for recommendation

    else:
        video = (get_object_or_404(Show, pk=video_id))
        # Sort latest_movies in ascending order based on premiere_date
        video_recs = Show.objects.all().order_by('premiere_date')[:6]
    return render(request, 'streaming/video_detail.html',
                  {'video': video, 'video_recs': video_recs})


# def video_detail(request, video_id):
#     video = get_object_or_404(Video, pk=video_id)
#     return render(request, 'streaming/video_detail.html', {'video': video})


def privacy_policy(request):
    return render(request, 'streaming/privacy_p.html')
