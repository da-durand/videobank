from django.db import models
from django.utils.translation import gettext_lazy as _
from modeltranslation.translator import TranslationOptions

class Movie(models.Model):
    label = models.CharField(max_length = 200, verbose_name = _('titre'))
    synopsis = models.CharField(max_length = 200, null = True)
    thumb = models.ImageField(upload_to='media', verbose_name = _('affiche'))
    director = models.CharField(max_length = 200, verbose_name = _('réalisateur'), null = True)

    def is_rented(self):
        return self.movie_rent.filter(date_return = None).count() >= 1



class MovieGenre(models.Model):
    label = models.CharField(max_length = 200)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, null=True)