from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import MovieRent
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from movie.models import Movie
import datetime


class MovieRentCreateView(DetailView):
    model = Movie

    def get(self, request, *args, **kwargs):

        MovieRent.objects.create(client = request.user.profile , movie = self.get_object())

        return HttpResponseRedirect(reverse_lazy('movie_list'))


class MovieRentListView(ListView):
    model = MovieRent
    template_name = "movie_rent_list.html"

class MovieReturnView(DetailView):
    model = MovieRent

    def get(self, request, *args, **kwargs):

        MovieRent.objects.filter(id=self.get_object().id).update(date_return= datetime.datetime.now())

        return HttpResponseRedirect(reverse_lazy('movie_list'))
