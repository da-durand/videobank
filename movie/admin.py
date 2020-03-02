from django.contrib import admin
from .models import Movie, MovieGenre
# Register your models here.

class MovieGenreAdmin(admin.StackedInline):
    model = MovieGenre
    can_delete = False
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieGenreAdmin]

admin.site.register(Movie, MovieAdmin)