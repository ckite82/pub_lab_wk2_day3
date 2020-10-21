import unittest
#import unittest is boilerplate language, must be included
from src.pub import Pub 
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

    def test_customer_can_buy_drink(self):
        customers = Customer("Colin", 20.00)
        self.assertEqual(3.00, drinks.price)
        self.assertEqual(17.00, customers.wallet)
        self.assertEqual(103.00, pub.till)




        # def test_can_sell_pet_to_customer(self):
        # customer = Customer("Jack Jarvis", 1000)
        # self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
        # self.assertEqual(1, customer.pet_count())
        # self.assertEqual(1, self.pet_shop.stock_count())
        # self.assertEqual(1, self.pet_shop.pets_sold)
        # self.assertEqual(1500, self.pet_shop.total_cash)