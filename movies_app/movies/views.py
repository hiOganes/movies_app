from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import MoviesModel
from .forms import RatingForm


def list_movie(request):
    value = request.GET.get('search', '')
    if value:
        movies = MoviesModel.objects.filter(title__istartswith=value)
    else:
        movies = MoviesModel.objects.all()
    paginator = Paginator(movies, 6)
    num_page = request.GET.get('page', 1)
    page_obj = paginator.page(num_page)
    form = RatingForm()
    return render(
        request, 
        'movies/search.html', 
        {'movies': page_obj, 'form': form}
        )


def detail_movie(request, movie_slug):
    movie = get_object_or_404(MoviesModel, slug=movie_slug)
    return render(request, 'movies/movie.html', {'movie': movie})


def rated_movie(request):
    movies = MoviesModel.objects.all()
    return render(request, 'movies/rated.html', {'movies': movies})
