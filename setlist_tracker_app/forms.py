from django import forms

from .models import Song, Link

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']
        labels = {'title': 'Title', 'artist': 'Artist'}

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'link_type', 'url']
        labels = {
            'name': 'Name',
            'link_type': 'Type',
            'url': 'URL'
        }
