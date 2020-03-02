from django.contrib import admin
from .models import MovieRent

class MovieRentAdmin(admin.ModelAdmin):
    model = MovieRent

admin.site.register(MovieRent, MovieRentAdmin)