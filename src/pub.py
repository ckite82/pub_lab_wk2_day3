class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_cash_to_till(self, amount):
        self.till += amount


    def check_age(self, age):
        if age >= 18:
            return True
        else:
            return False
    

    def customer_can_buy_drink(self, drinks, customer):
        # drinks.price == price
        customer.remove_money_from_wallet(drinks.price)
        self.add_cash_to_till(drinks.price)
    
    # def check_drunkenness(self, drunkenness_level):
    #     if customer.drunkenness_level >= 6:
    #         return True
    #     else:
    #         return False