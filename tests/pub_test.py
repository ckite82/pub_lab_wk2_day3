import unittest
#import unittest is boilerplate language, must be included
from src.pub import Pub 
from src.customers import Customer
from src.drinks import Drink
#from src is the source folder/directory and .pub must exactly reflect name.
#import Pub is a capital as it is the class name that is being imported

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_add_cash_to_till(self):
        self.pub.add_cash_to_till(3.00)
        self.assertEqual(103.00, self.pub.till)

    def test_check_over_age_true(self):
        customer = Customer("Colin", 20.00, 25)
        customer_is_old_enough = self.pub.check_age(customer.age)
        self.assertEqual(True, customer_is_old_enough)

    def test_check_over_age_false(self):
        customer = Customer("Ed", 20.00, 17)
        customer_is_old_enough = self.pub.check_age(customer.age)
        self.assertEqual(False, customer_is_old_enough)



    def test_customer_can_buy_drink(self):
        customer = Customer("Colin", 20.00, 25)
        drink = Drink("Tennants", 3.00)
        self.pub.customer_can_buy_drink(drink, customer)
        self.assertEqual(3.00, drink.price)
        self.assertEqual(17.00, customer.wallet)
        self.assertEqual(103.00, self.pub.till)
