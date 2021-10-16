"""Defines URL patterns for setlist_tracker_app."""

from django.urls import path

from . import views

app_name = 'setlist_tracker_app'
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # View all songs
    path('songs/', views.songs, name='songs'),
    # View links for a specific song
    path('song/<int:song_id>/', views.song, name='song'),
    # create new song
    path('new_song/', views.new_song, name='new_song'),
    # delete existing song
    path('delete_song/<int:song_id>', views.delete_song, name='delete_song'),
    # create new song
    path('new_link/<int:song_id>/', views.new_link, name='new_link'),
    # delete existing link
    path('delete_link/<int:song_id>/<int:link_id>/', views.delete_link, name='delete_link'),
]
