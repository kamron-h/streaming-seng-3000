from django import forms

from streaming.models import Video, Actor, Rating


# Video form
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'video', 'thumbnail')  # specify the fields from the Video model


# Actor form
class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('name',)  # specify the fields from the Actor model


# Rating form
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)  # specify the fields from the Rating model
