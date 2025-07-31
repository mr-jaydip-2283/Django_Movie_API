from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django Movie API is running successfully 🚀")


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer