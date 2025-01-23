class Product:
    def __init__(self, name, price, initial_stock):
        self.name = name
        self.price = price
        self.stock = initial_stock
        self.available = True

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def is_available(self):
        return self.available

    def set_availability(self, available):
        self.available = available

    def has(self, stock):
        return self.stock >= stock

    def sell(self, amount):
        self.stock -= amount
        return amount * self.price

    def restock(self, amount):
        self.stock += amount

    def prune(self):
        self.stock = 0

    def __str__(self):
        return f"{self.name} at ${self.formatted(self.price)} ({self.stock})"

    def formatted(self, price):
        return "{:,.2f}".format(price)

