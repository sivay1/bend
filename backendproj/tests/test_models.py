from django.test import TestCase
from restaurant.models import Menu,Booking

class MenuItemTest(TestCase):
	def test_get_item(self):
		# Create a MenuItem instance
		item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        # Get the string representation of the MenuItem instance
		item_str = str(item)

        # Assert that the string representation matches the expected value
		expected_str = "IceCream : 80"
		self.assertEqual(item_str, expected_str)

