from django.shortcuts import render, HttpResponse
from .models import Movie

# Create your views here.
def root(request):
    context = {
       'movies': Movie.objects.all()
    }
    return render(request, 'index.html', context)