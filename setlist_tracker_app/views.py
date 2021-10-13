from django.shortcuts import render

from .models import Song
from .models import Link

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