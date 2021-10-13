from django.db import models

# Create your models here.
class Song(models.Model):
    """Represents a song that I know how to play, sort of"""
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    # chords = models.CharField(max_length=200)
    # lyrics = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

class Link(models.Model):
    """Represents a helpful link to something about a song I know"""
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    PERFORMANCE = "P"
    TUTORIAL = "T" 
    TYPE_CHOICES = [
        (PERFORMANCE, "Performance"),
        (TUTORIAL, "Tutorial"),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=PERFORMANCE,
    )
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.type}"
