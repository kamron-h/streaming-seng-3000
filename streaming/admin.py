from django.contrib import admin
from .models import Video, Actor, Playlist, Genre, Rating, Comment

# Register your models here.
admin.site.register(Video)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Playlist)
