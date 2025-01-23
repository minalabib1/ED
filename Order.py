class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return ""

