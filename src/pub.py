class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_cash_to_till(self, amount):
        self.till += amount

    def customer_can_buy_drink(self, drinks, customer):
        drinks.price == price
        customers.remove_money_from_wallet()
        self.add_cash_to_till()
        
    # def sell_pet_to_customer(self, name_of_pet, customer):
    #     pet_to_buy = self.find_pet_by_name(name_of_pet)         # find pet in shop gives pet object
    #     self.remove_pet(pet_to_buy)                             # remove pet from shop
    #     customer.add_pet(pet_to_buy)                            # add pet to customer
    #     self.increase_pets_sold()                               # increase number of pets sold
    #     customer.remove_money(pet_to_buy.price)                 # - removing cash from customer 
    #     self.increase_total_cash(pet_to_buy.price)              # increase shops total cash