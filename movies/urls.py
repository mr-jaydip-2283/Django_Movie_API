# movies/urls.py
from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView,home

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy'),
    path('', home),
]