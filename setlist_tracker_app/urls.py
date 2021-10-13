"""Defines URL patterns for setlist_tracker_app."""

from django.urls import path

from . import views

app_name = 'setlist_tracker_app'
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('songs/', views.songs, name='songs'),
    path('song/<int:song_id>/', views.song, name='song'),
]
