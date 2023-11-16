from django.contrib import admin
from .models import Movie, Actor, Playlist, Genre, Rating, \
    Comment, Show, ShowActorRole, Episode, Language, Season, \
    Country, Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(Show)
admin.site.register(ShowActorRole)
admin.site.register(Episode)
admin.site.register(Language)
admin.site.register(Season)
admin.site.register(Country)
