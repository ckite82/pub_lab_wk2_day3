class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = 0

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def drunkenness_level_increased(self, drink):
        self.drunkenness_level += drink.alcohol_level