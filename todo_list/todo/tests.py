import logging

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from todo.models import Todo
from todo.serializers import TodoSerializer

logging.basicConfig()
logger = logging.getLogger('TestAPI')
logger.setLevel(logging.INFO)


class TestAPI(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create a test instance of Todo
        self.test_todo = Todo.objects.create(
            title='Test Title',
            description='Test description',
            due_date=None,
            completed_date=None,
            priority='low'
        )
        self.list_url = reverse('list-todos')
        self.detail_url = reverse('get-todo', args=[
            self.test_todo.id
        ])
        self.not_found_detail_url = reverse('get-todo', args=[
            '0'
        ])

    def test_get_all_todos(self):
        """Test fetching all todos."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_to_do(self):
        """Test fetching one todo instance."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_404_code(self):
        """Test 404 not found response."""
        response = self.client.get(self.not_found_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
