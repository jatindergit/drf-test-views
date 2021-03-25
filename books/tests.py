from rest_framework.test import APIRequestFactory
from django.core.management import call_command
from django.urls import reverse
from rest_framework.test import APITestCase
from books.views import ListCreateBookView
from books.models import Book


class AccountTests(APITestCase):

    def setUp(self):
        call_command('loaddata', 'books/fixtures/initial_data.json')
        self.url = reverse('books-list')

    def test_book_list(self):
        view = ListCreateBookView.as_view()
        factory = APIRequestFactory()
        request = factory.get(self.url)
        response = view(request, pk='1')
        response.render()
        self.assertEqual(response.content,
                         b'[{"id":1,"title":"C Plus Plus","author":"E Balaguruswami","published_on":"2021-03-25"}]')

    def test_create_book(self):
        view = ListCreateBookView.as_view()
        factory = APIRequestFactory()
        request = factory.post(self.url,
                               {'title': 'Java Head First', 'author': 'English Man', 'published_on': '2011-07-15'},
                               format='json')
        _ = view(request)
        self.assertTrue(Book.objects.filter(title='Java Head First').exists())
