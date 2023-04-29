from shopping_cart import ShoppingCart


class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance
        self.shopping_cart = ShoppingCart()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, balance):
        self.account_balance = balance
