def remove_product(self, name):
    self.products = [product for product in self.products if product.name != name]
