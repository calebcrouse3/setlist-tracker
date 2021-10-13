"""Defines URL patterns for setlist_tracker_app."""

from django.urls import path

from . import views

app_name = 'setlist_tracker_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
