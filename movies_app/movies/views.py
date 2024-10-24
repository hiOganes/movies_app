from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import MoviesModel


def list_movie(request):
    movies = MoviesModel.objects.filter(
        title__istartswith=request.GET.get('search', '')
        )
    paginator = Paginator(movies, 6)
    num_page = request.GET.get('page', 1)
    page_obj = paginator.page(num_page)
    return render(
        request, 
        'movies/search.html', 
        {'movies': page_obj,}
        )


def detail_movie(request, movie_slug):
    movie = get_object_or_404(MoviesModel, slug=movie_slug)
    return render(request, 'movies/movie.html', {'movie': movie})


def rated_movie(request):
    movies = MoviesModel.objects.all()
    return render(request, 'movies/rated.html', {'movies': movies})
