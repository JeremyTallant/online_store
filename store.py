from product import Product
from shopping_cart import ShoppingCart


class Store:
    def __init__(self):
        self.products = [
            Product(1, "Laptop", "A high-performance laptop", 1200.00, 10),
            Product(2, "Smartphone", "A feature-packed smartphone", 800.00, 15),
            Product(3, "Headphones", "Noise-cancelling headphones", 150.00, 25),
        ]

    def browse(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(f"{product.id}. {product.name} - ${product.price} - {product.description}")

    def add_to_cart(self, product_id, shopping_cart: ShoppingCart):
        for product in self.products:
            if str(product.id) == product_id:
                shopping_cart.add_item(product)
                print(f"\n{product.name} added to your cart.")
                return
        print("\nInvalid product ID. Please try again.")

    def remove_from_cart(self, product_id, shopping_cart: ShoppingCart):
        for product in shopping_cart.items:
            if str(product.id) == product_id:
                shopping_cart.remove_item(product)
                print(f"\n{product.name} removed from your cart.")
                return
        print("\nInvalid product ID. Please try again.")

    def checkout(self, user):
        cart_total = user.shopping_cart.calculate_total()
        if cart_total <= user.account_balance:
            user.account_balance -= cart_total
            user.shopping_cart.clear()
            print(f"\nCheckout successful! Your new account balance is ${user.account_balance:.2f}.")
        else:
            print("\nInsufficient funds. Please remove some items from your cart or add funds to your account.")
