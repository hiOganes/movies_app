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
        'Checking the search field'
        path = reverse('search')
        test_data = ['title', 'title1', 'title11', 'non-existent_value']

        for elem in test_data:
            response = self.client.get(path + '?search=' + elem)
            data_db = MoviesModel.objects.filter(title__istartswith=elem)
            self.assertQuerySetEqual(
                response.context['movies'].object_list, 
                data_db[(response.context['movies'].number-1)*6:6]
                )

    def tearDown(self):
        pass