from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for setlist tracker."""
    return render(request, 'setlist_tracker_app/index.html')