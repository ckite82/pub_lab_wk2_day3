import unittest

from src.customers import Customer 
from src.drinks import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customers = Customer("Colin", 20.00, 25)
        self.drink = Drink("Tennents", 3.00, 2)

    def test_customer_has_name(self):
        self.assertEqual("Colin", self.customers.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customers.wallet)

    def test_remove_money_from_wallet(self):
        self.customers.remove_money_from_wallet(3.00)
        self.assertEqual(17.00, self.customers.wallet)

    def test_drunkenness_level_zero(self):
        self.assertEqual(0, self.customers.drunkenness_level)

    def test_drunkenness_level_increased(self):
        self.customers.drunkenness_level_increased(self.drink)
        self.assertEqual(2, self.customers.drunkenness_level)