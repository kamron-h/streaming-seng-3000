from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    actors = models.ManyToManyField('Actor', related_name='videos', blank=True)
    comments = models.ManyToManyField('Comment', related_name='comments', blank=True)
    ratings = models.ManyToManyField('Rating', related_name='ratings', blank=True)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return str(self.rating)


class Genre(models.Model):
    genre = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='genres')

    def __str__(self):
        return self.genre


#
# class Director(models.Model):
#     name = models.CharField(max_length=100)
#     video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='directors')
#
#     def __str__(self):
#         return self.name
#
#
# class Publisher(models.Model):
#     name = models.CharField(max_length=100)
#     video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='publishers')
#
#     def __str__(self):
#         return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='playlists')
    thumbnail = models.ImageField(upload_to='thumbnail_pictures/', null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    GENRES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Biography', 'Biography'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Film-Noir', 'Film-Noir'),
        ('History', 'History'),
        ('Horror', 'Horror'),
        ('Music', 'Music'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Sport', 'Sport'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
        ('Journalism', 'Journalism'),
        ('Black Exploitation', 'Black Exploitation'),
        ('Editors Favorite', 'Editors Favorite'),
        ('Other', 'Other'),
    ]
