from django.forms import ModelForm
from models import *



class GenreForm(ModelForm):
    class Meta:
        model = Genre

class MovieForm(ModelForm):
    class Meta:
        model = Movie

class ActorForm(ModelForm):
    class Meta:
        model = Actor
