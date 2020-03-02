from django.db import models
from movie.models import Movie
from client.models import MyProfile

class MovieRent(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, null=True, related_name='movie_rent')
    client = models.ForeignKey(MyProfile, on_delete = models.CASCADE, null=True, related_name='movie_rent')
    date_out = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(null=True, blank=True)
