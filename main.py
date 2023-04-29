from store import Store
from user import User


class Main:
    def __init__(self):
        self.store = Store()
        
        print("Welcome to the online store!")
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        starting_balance = float(input("Enter your starting dollar amount: "))

        self.user = User(name, email, starting_balance)

    def run(self):
        while True:
            print("\nWelcome to the Online Store!")
            print("1. Browse products")
            print("2. View cart")
            print("3. Checkout")
            print("4. Load money")
            print("5. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.store.browse()
                product_id = input("Enter the ID of the product you'd like to add to your cart (or 'q' to go back): ")
                if product_id.lower() != 'q':
                    self.store.add_to_cart(product_id, self.user.shopping_cart)
            elif choice == "2":
                self.user.shopping_cart.view_cart()
            elif choice == "3":
                self.store.checkout(self.user)
            elif choice == '4':
                amount = float(input("Enter the amount of fake money you'd like to load: "))
                self.user.load_fake_money(amount)
            elif choice == "5":
                print("Thank you for shopping with us. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    Main()
