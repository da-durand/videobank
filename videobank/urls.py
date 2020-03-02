"""videobank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie.views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView
from location.views import MovieRentCreateView, MovieRentListView, MovieReturnView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('userena.urls')),
    path('', MovieListView.as_view(), name="movie_list"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('movie/<int:pk>/edit', MovieUpdateView.as_view(), name="movie_update"),
    path('movie/<int:pk>/delete', MovieDeleteView.as_view(), name="movie_delete"),
    path('movie/add/', MovieCreateView.as_view(), name="movie_create"),
    path('movierent/<int:pk>', MovieRentCreateView.as_view(), name="movie_rent_create"),
    path('moviereturn/<int:pk>', MovieReturnView.as_view(), name="movie_return"),
    path('movierents', MovieRentListView.as_view(), name="movie_rent_list"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n'), name = "set_language"),
]