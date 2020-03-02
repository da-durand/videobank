from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Movie
from django.urls import reverse_lazy


class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"

class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie_form.html"
    fields = "__all__"
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "movie_form.html"
    fields = "__all__"
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')
