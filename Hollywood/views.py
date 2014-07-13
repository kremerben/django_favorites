from django.shortcuts import render, render_to_response, redirect
from django.forms import ModelForm

from models import *
from forms import *
# Create your views here.

def home(request):
    return render_to_response("home.html")

def genres(request):
    genres = Genre.objects.all()
    return render_to_response("genre/genres.html", {'genres': genres})

def movies(request):
    movies = Movie.objects.all()
    return render_to_response("movie/movies.html", {'movies': movies})

def actors(request):
    actors = Actor.objects.all()
    return render_to_response("actor/actors.html", {'actors': actors})

#
# class GenreForm(ModelForm):
#     class Meta:
#         model = Genre


def new_genre(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = GenreForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/genres")

    # Else if the user is looking at the form page
    else:
        form = GenreForm()
    data = {'form': form}
    return render(request, "genre/new_genre.html", data)

def new_movie(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = MovieForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/movies")

    # Else if the user is looking at the form page
    else:
        form = MovieForm()
    data = {'form': form}
    return render(request, "movie/new_movie.html", data)

def new_actor(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = ActorForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/actors")

    # Else if the user is looking at the form page
    else:
        form = ActorForm()
    data = {'form': form}
    return render(request, "actor/new_actor.html", data)


def view_actor(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    data = {"actor": actor}
    return render(request, "actor/view_actor.html", data)

def view_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    data = {"genre": genre}
    return render(request, "genre/view_genre.html", data)

def view_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    actor = Actor.objects.all()
    data = {"movie": movie, "actor":actor}
    return render(request, "movie/view_movie.html", data)



def edit_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            if form.save():
                return redirect("/genres/{}".format(genre_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(instance=genre)
    data = {"genre": genre, "form": form}
    return render(request, "genre/edit_genre.html", data)

def edit_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            if form.save():
                return redirect("/movies/{}".format(movie_id))
    else:
        form = MovieForm(instance=movie)
    data = {"movie": movie, "form": form}
    return render(request, "movie/edit_movie.html", data)

def edit_actor(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            if form.save():
                return redirect("/actors/{}".format(actor_id))
    else:
        form = ActorForm(instance=actor)
    data = {"actor": actor, "form": form}
    return render(request, "actor/edit_actor.html", data)

def delete_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    genre.delete()
    return redirect("/genres")

def delete_actor(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    actor.delete()
    return redirect("/actors")

def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("/movies")