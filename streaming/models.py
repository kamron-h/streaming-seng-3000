from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# from django.core.exceptions import ValidationError


RATINGS_CHOICES = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC', 'NC'), ('TV', 'TV'))
QUALITY_CHOICES = (('CAM', 'CAM'), ('SD', 'SD'), ('HD', 'HD'), ('UHD', 'UHD'),)
TYPE_CHOICES = (('Movie', 'Movie'), ('Show', 'Show'))
REGION_CHOICES = (
    ('Africa', 'Africa'),
    ('Asia', 'Asia'),
    ('Europe', 'Europe'),
    ('US', 'US'),
    ('Australia', 'Australia'),
    ('North America', 'North America'),
    ('South America', 'South America'),
    ('Central America', 'Central America'),
    ('North East Africa', 'North East Africa'),
    ('Caribbean', 'Caribbean'),
)


# Create member model with attributes
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True, blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='M', blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=35, null=True, blank=True)
    state = models.CharField(max_length=14, null=True, blank=True)
    zipcode = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=40, unique=True)
    premiere_date = models.DateField(null=True, blank=True)  # The date when the show first aired
    description = models.TextField(null=True, blank=True)
    length = models.CharField(max_length=30, null=True, blank=True)
    rating = models.CharField(max_length=5, choices=RATINGS_CHOICES, default='R')
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Movie')
    quality = models.CharField(max_length=5, choices=QUALITY_CHOICES, default='HD')
    region = models.CharField(max_length=50, choices=REGION_CHOICES, default='US')
    genres = models.ManyToManyField('Genre', blank=True)
    cast = models.ManyToManyField('Actor', blank=True)
    language = models.ManyToManyField('Language', blank=True)
    country = models.ManyToManyField('Country', blank=True)
    budget = models.CharField(max_length=15, null=True, blank=True)
    box_office = models.CharField(max_length=100, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    trailer_id = models.CharField(max_length=150, null=True, blank=True)  # URL to the show's trailer (if available)
    trailer_url = models.URLField(null=True, blank=True)  # URL to the show's trailer (if available)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Show(models.Model):
    title = models.CharField(max_length=30, unique=True)  # Title of the show
    premiere_date = models.DateField(null=True, blank=True)  # The date when the show first aired
    end_date = models.DateField(null=True, blank=True)  # The date when the show ended (if it has ended)
    description = models.TextField(null=True, blank=True)  # A brief description or synopsis
    length = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Show')
    quality = models.CharField(max_length=5, choices=QUALITY_CHOICES, default='HD')  # Quality of the show
    rating = models.CharField(max_length=10, choices=RATINGS_CHOICES, default='R')
    country = models.ManyToManyField('Country', blank=True)  # Country of the show
    language = models.ManyToManyField('Language', blank=True) # Language of the show
    comments = models.ManyToManyField('Comment', related_name='show_comments', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)  # Genres associated with the show
    cast = models.ManyToManyField('Actor', through='ShowActorRole', blank=True)  # Cast members and their roles in the show
    episodes = models.ManyToManyField('Episode', blank=True, related_name='season_episodes')  # Seasons associated with
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)  # Cover image or poster for the show
    trailer_id = models.CharField(max_length=150, null=True, blank=True)  # URL to the show's trailer (if available)
    trailer_url = models.URLField(null=True, blank=True)  # URL to the show's trailer (if available)
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp when the show entry was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the show entry was last updated

    def __str__(self):
        return self.title


class ShowActorRole(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)  # Character name or role description

    class Meta:
        unique_together = ('actor', 'show')

    def __str__(self):
        return f"{self.actor.name} as {self.role} in {self.show.title}"


class Episode(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='episode_set')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    trailer_id = models.CharField(max_length=150, null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    rating = models.CharField(max_length=5, choices=RATINGS_CHOICES, default='R')
    comments = models.ManyToManyField('Comment', related_name='episode_comments', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    episode_number = models.PositiveIntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)


# Create a Season model
class Season(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    episodes = models.ManyToManyField('Episode', blank=True, related_name='season_set')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True, default=timezone.now)
    duration = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Actor(models.Model):
    name = models.CharField(max_length=30, unique=True)
    birthdate = models.DateField(null=True, blank=True)
    movies = models.ManyToManyField('Movie', blank=True)
    shows = models.ManyToManyField('Show', blank=True)
    country = models.ManyToManyField('Country', blank=True)  # Country of the show
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    # TODO: Remove the 'profile_img' field
    thumbnail_url = models.URLField(null=True, blank=True)
    profile_img = models.URLField(null=True, blank=True)
    profile_img_url = models.URLField(null=True, blank=True)
    bio = models.TextField(max_length=3000, null=True, blank=True)
    networth = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Comment(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('archived', 'Archived'),
        ('deleted', 'Deleted'),
    ]
    user = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.message


class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return str(self.rating)


class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    region = models.CharField(max_length=20, choices=REGION_CHOICES, default='North America')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.country


class Genre(models.Model):
    genre = models.CharField(max_length=20, unique=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    region = models.CharField(max_length=20, choices=REGION_CHOICES, default='North America')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language


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


# Playlist video relationship needs to be revised to handle both movies and tv shows
class Playlist(models.Model):
    name = models.CharField(max_length=20)
    video = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='playlists')
    thumbnail_url = models.ImageField(upload_to='thumbnail_pictures/', null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
