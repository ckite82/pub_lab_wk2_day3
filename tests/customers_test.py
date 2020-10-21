import unittest
#import unittest is boilerplate language, must be included
from src.customers import Customer 

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customers = Customer("Colin", 20.00, 25)

    def test_customer_has_name(self):
        self.assertEqual("Colin", self.customers.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customers.wallet)

    def test_remove_money_from_wallet(self):
        self.customers.remove_money_from_wallet(3.00)
        self.assertEqual(17.00, self.customers.wallet)