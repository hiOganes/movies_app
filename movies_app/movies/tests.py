from django.test import TestCase
from http import HTTPStatus
from django.shortcuts import reverse

from .models import MoviesModel


class FindMovie(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        pass
    
    def test_search_page(self):
        'Checking the main page'
        path = reverse('search')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_movie_page(self):
        'Checking the movies detailed description page'
        movie_slug = MoviesModel.objects.get(pk=1).slug
        path = reverse('movie', kwargs={'movie_slug': movie_slug})
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_search_bar(self):
        pass

    def tearDown(self):
        pass