from product_manager import ProductManager
from product import Product

manager = ProductManager()


manager.add_product(Product("Laptop", 3000, 5))
manager.add_product(Product("Mouse", 100, 10))
manager.add_product(Product("Keyboard", 200, 7))


manager.display_products()


print(f"Total inventory value: {manager.total_value()} RON")

