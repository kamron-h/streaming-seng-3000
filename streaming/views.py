from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

# Create your views here.
from streaming.forms import VideoForm, ActorForm
from streaming.models import Actor, Video

CRUD_URL = 'streaming/crud.html'


def crud(request, model_type=None, entry_id=None):
    ModelForm = VideoForm if model_type == "videos" else ActorForm
    Model = Video if model_type == "videos" else Actor
    videos = Video.objects.all()
    actors = Actor.objects.all()

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
        if instance:
            form = ModelForm(request.PUT, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect(CRUD_URL)
        else:
            return HttpResponse("Invalid request", status=400)

    # Handle DELETE request (For both Video and Actor deletion)
    elif request.method == 'DELETE':
        if instance:
            instance.delete()
            return redirect(CRUD_URL)
        else:
            return HttpResponse("Invalid request", status=400)

    # Handle GET request
    else:
        form = ModelForm(instance=instance)

    # Render the page with the form as context
    return render(request, CRUD_URL, {'form': form, 'videos': videos, 'actors': actors})


def api_index(request):
    return render(request, 'streaming/api_index.html')


def home(request):
    return render(request, 'streaming/home.html')
