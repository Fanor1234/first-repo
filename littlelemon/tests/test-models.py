from django.test import TestCase
from restaurant.models import MenuTable

#TestCase class
class MenuTableTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item, "IceCream : 80")