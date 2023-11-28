from django import forms

from streaming.models import Movie, Actor, Rating


# Video form
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'thumbnail_url', 'trailer_url')  # specify the fields from the Video model



# Actor form
class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('name', 'profile_img_url')  # specify the fields from the Actor model


# Rating form
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        # specify all fields of the Rating model
        fields = ('rating',)
