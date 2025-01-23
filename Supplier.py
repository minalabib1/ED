from Products import Products

class Supplier:
    def __init__(self, name, region, address, products):
        self.name = name
        self.region = region
        self.address = address
        # Use the correct class name `Products`, not `products`.
        self.products = Products(products)
        self.profit = 0
        self.menu_options = ["1. View supplier details", "2. View products", 
                             "3. View profit", "4. Order"]
        self.manager_options = ["1. View supplier details", "2. View all products", 
                                "3. View available products", "4. Add a product", 
                                "5. Remove a product", "6. Restock a product", 
                                "7. Delist a product", "8. View profit", "9. Order"]

    def get_products(self):
        return self.products

    def add_profit(self, amount):
        self.profit += amount

    def use(self, user):
        while True:
            print(f"Welcome to {self.name}")
            for option in self.menu_options:
                print(option)  # Ensure no extra prints after this
            choice = input("Please enter a choice: ")

            if choice == "1":
                print(self)
            elif choice == "2":
                print(self.products)
            elif choice == "3":
                print(f"Total Profit: {self.formatted(self.profit)}")
            elif choice == "4":
                cart = Cart(self, user)
                cart.use()
            elif choice == "X":
                print(f"Thanks for shopping at {self.name}")  # No extra new line needed
                break
            else:
                print("Please enter a valid number, or press X to exit.")

    
    def manage(self, user):
        while True:
            print(f"Welcome to {self.name}")
            for option in self.manager_options:
                print(option)
            choice = input("Please enter a choice: ")

            if choice == "1":
                print(self)
            
            elif choice == "2":
                print(self.products)
            
            elif choice == "3":
                self.products.print_available_products()
            
            elif choice == "4":
                input_name = input("Name: ")
                input_price = float(input("Price: "))
                initial_stock = int(input("Initial stock: "))
                new_product = Product(input_name, input_price, initial_stock)
                self.products.add_product(new_product)
            
            elif choice == "5":
                input_name = input("Name: ")
                removed_product = self.products.remove_product(input_name)
                if removed_product:
                    print(f"{input_name} successfully removed.")
                else:
                    print("No such product. Try again.")
            
            elif choice == "6":
                input_name = input("Name: ")
                product_found = self.products.find_product(input_name)
                if product_found:
                    input_amount = int(input("Amount: "))
                    product_found.restock(input_amount)
                    print(f"{input_name} successfully updated.")
                else:
                    print("No such product. Try again.")
            
            elif choice == "7":
                input_name = input("Name: ")
                product_found = self.products.find_product(input_name)
                if product_found:
                    product_found.set_availability(False)
                    print(f"{input_name} successfully delisted.")
                else:
                    print("No such product. Try again.")
            
            elif choice == "8":
                print(f"Total Profit: {self.formatted(self.profit)}")
            
            elif choice == "9":
                cart = Cart(self, user)
                cart.use()
            
            elif choice == "X":
                break

            else:
                print("Please enter a valid number, or press X to exit.")
    
    def get_region(self):
        return self.region

    def __str__(self):
        return f"{self.name} ({self.region}), {self.address}"

    def formatted(self, price):
        return "{:,.2f}".format(price)


