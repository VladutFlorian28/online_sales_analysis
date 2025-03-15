from cart import Cart

cart = Cart()
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

cart.display_cart()
print(f"Total cart value: {cart.total_cart_value()} RON")
