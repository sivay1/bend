from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title='Dish1', price=10.0,inventory = 1)
        Menu.objects.create(title='Dish2', price=15.0,inventory = 11)
        Menu.objects.create(title='Dish3', price=20.0,inventory = 12)

        # Initialize the Django REST framework API client
        self.client = APIClient()

    def test_getall(self):
        # Retrieve all Menu objects using the MenuView API endpoint
        url = reverse('menu-view')  # Assuming 'menu-list' is the name of your MenuView URL
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data using the MenuSerializer
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        expected_data = serializer.data

        # Check that the response data matches the expected data
        self.assertEqual(response.data, expected_data)
