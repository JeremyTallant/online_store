class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def calculate_total(self):
        total = 0.0
        for item in self.items:
            total += item.get_price()
        return total

    def clear(self):
        self.items = []

    def view_cart(self):
        if not self.items:
            print("\nYour cart is empty.")
            return

        print("\nItems in your cart:")
        for item in self.items:
            print(f"{item.get_id()}. {item.get_name()} - ${item.get_price()} - {item.get_description()}")

        total = self.calculate_total()
        print(f"\nTotal: ${total:.2f}")
