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

`main.py`: The main script that initializes the store, user, and provides a command-line interface for users to interact with the store
`store.py`: Contains the `Store` class definition, which manages product listings and shopping cart operations
`product.py`: Contains the `Product` class definition, which represents individual products in the store
`shopping_cart.py`: Contains the `ShoppingCart` class definition, which represents a user's shopping cart and provides methods for managing items in the cart
`user.py`: Contains the `User` class definition, which stores user information, account balance, and a shopping cart instance
`products.json`: A JSON file containing example product data for the store
