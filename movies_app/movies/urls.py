from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.list_movie, name='search'),
    path('rated/', views.rated_movie, name='rated'),
    path('movie/<slug:movie_slug>/', views.detail_movie, name='movie'),
]