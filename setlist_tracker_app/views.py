from django.shortcuts import render, redirect

from .models import Song, Link
from .forms import SongForm, LinkForm


# Create your views here.
def home(request):
    """The home page for setlist tracker."""
    return render(request, 'setlist_tracker_app/home.html')


def songs(request):
    """A users list of songs"""
    songs = Song.objects.order_by("title")
    context = {"songs": songs}
    return render(request, 'setlist_tracker_app/songs.html', context)


def song(request, song_id):
    """See links for a single song"""
    song = Song.objects.get(id=song_id)
    links = song.link_set.order_by("name")
    context = {'song': song, 'links': links}
    return render(request, 'setlist_tracker_app/song.html', context)


def new_song(request):
    """Add a new song"""
    if request.method != 'POST':
        form = SongForm()
    else:
        form = SongForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('setlist_tracker_app:songs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'setlist_tracker_app/new_song.html', context)


def new_link(request, song_id):
    """Add a new link for a particular song"""
    song = Song.objects.get(id=song_id)

    if request.method != 'POST':
        form = LinkForm()
    else:
        form = LinkForm(data=request.POST)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.song = song
            new_link.save()
            return redirect('setlist_tracker_app:song', song_id=song_id)  # how to redirect to song_id?

    # Display a blank or invalid form.
    context = {'song': song, 'form': form}
    return render(request, 'setlist_tracker_app/new_link.html', context)


def delete_song(request, song_id):
    # delete the song
    Song.objects.get(id=song_id).delete()
    return redirect('setlist_tracker_app:songs')

def delete_link(request, song_id, link_id):
    # delete the song
    Link.objects.get(id=link_id).delete()
    return redirect('setlist_tracker_app:song', song_id=song_id)
