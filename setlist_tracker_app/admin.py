from django.contrib import admin

# Register your models here.
from .models import Song, Link

admin.site.register(Song)
admin.site.register(Link)
