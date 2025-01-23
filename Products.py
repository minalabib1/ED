class Products:
    def __init__(self, initial_products=None):
        if initial_products is None:
            self.products = []
        else:
            self.products = initial_products

    def __str__(self):
        # Join all products with a newline, without adding an extra newline at the end
        return "\n".join([str(product) for product in self.products])

    def print_products_with_numbers(self):
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.get_name()} at ${product.get_price()} ({product.stock} available)")

    def print_available_products(self):
        for product in self.products:
            if product.is_available():
                print(f"{product.get_name()} at ${product.get_price()} ({product.stock} available)")

    def get_product_from_index(self, index):
        try:
            return self.products[index - 1]
        except IndexError:
            raise IndexError("No product found at that index!")

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for i, product in enumerate(self.products):
            if product.get_name() == product_name:
                self.products.pop(i)
                return True
        return False

    def find_product(self, product_name):
        for product in self.products:
            if product.get_name() == product_name:
                return product
        return None

