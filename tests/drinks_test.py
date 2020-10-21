import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drinks = Drink("Tennants", 3.00)

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drinks.name)

    def test_drink_has_price(self):
        self.assertEqual(3.00, self.drinks.price)