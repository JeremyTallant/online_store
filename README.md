# Online Store Project
## Description
This online store project is a simple Python-based command-line application that demonstrates object-oriented programming principles. It allows users to interact with a virtual store, where they can browse products, add items to their shopping cart, remove items, view their cart, and checkout. Users can also load fake money into their account to simulate purchasing items. The project uses classes and objects to represent various components, such as products, shopping carts, and users, showcasing the practical application of object-oriented programming.
## Features
* Browse a list of available products
* Add and remove products from the shopping cart
* View the shopping cart with a list of items and the total cost
* Load fake money into the user's account
* Checkout and simulate purchasing items using the user's account balance
## Project Structure
The project is organized into the following files:

* `main.py`: The main script that initializes the store, user, and provides a command-line interface for users to interact with the store
* `store.py`: Contains the `Store` class definition, which manages product listings and shopping cart operations
* `product.py`: Contains the `Product` class definition, which represents individual products in the store
* `shopping_cart.py`: Contains the `ShoppingCart` class definition, which represents a user's shopping cart and provides methods for managing items in the cart
* `user.py`: Contains the `User` class definition, which stores user information, account balance, and a shopping cart instance
* `products.json`: A JSON file containing example product data for the store
## How to Run the Application
1. Ensure that you have Python 3 installed on your computer.

2. Clone the repository or download the source files.

3. Open a terminal or command prompt, and navigate to the project directory.

4. Run the following command:
``` python
python main.py
```
5. Follow the prompts to enter your name, email address, and starting dollar amount.

6. Use the provided options to interact with the store, such as browsing products, adding items to your cart, and checking out.
## Customizing the Product List
You can customize the list of available products by editing the `products.json` file. Add or modify the product entries as needed, following the existing structure:
``` json
[
  {
    "id": "1",
    "name": "Product Name",
    "description": "Product description",
    "price": 19.99,
    "quantity": 10
  },
  ...
]
```
Make sure to maintain the JSON format and update the `id`, `name`, `description`, `price`, and `quantity` fields accordingly for each product.
## Contributing
Feel free to submit pull requests or report issues to help improve the project. All contributions are welcome!
