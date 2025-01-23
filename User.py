
class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.purchases = []

    def get_first_name(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def add_purchase(self, cart):
        self.purchases.append(cart)

    def use(self, org):
        pass  # Will be overridden by child classes

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


