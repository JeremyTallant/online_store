import tkinter as tk
from tkinter import messagebox
from store import Store
from user import User


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.store = Store()
        self.user = User("John Doe", "john.doe@example.com", 500.0)

        self.title("Online Store")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Welcome to the Online Store!").pack(pady=10)

        browse_button = tk.Button(self, text="Browse Products", command=self.browse_products)
        browse_button.pack(fill=tk.X, padx=20, pady=5)

        view_cart_button = tk.Button(self, text="View Cart", command=self.view_cart)
        view_cart_button.pack(fill=tk.X, padx=20, pady=5)

        checkout_button = tk.Button(self, text="Checkout", command=self.checkout)
        checkout_button.pack(fill=tk.X, padx=20, pady=5)

        exit_button = tk.Button(self, text="Exit", command=self.quit)
        exit_button.pack(fill=tk.X, padx=20, pady=5)

    def browse_products(self):
        self.store.browse()
        product_id = input("Enter the ID of the product you'd like to add to your cart (or 'q' to go back): ")
        if product_id.lower() != 'q':
            self.store.add_to_cart(product_id, self.user.shopping_cart)

    def view_cart(self):
        self.user.shopping_cart.view_cart()

    def checkout(self):
        self.store.checkout(self.user)

    def quit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
