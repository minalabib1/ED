import decimal

class Cart:
    def __init__(self, supplier, user):
        self.supplier = supplier
        self.user = user
        self.orders = []
        self.menu_options = ["1. Add a product to your cart", 
                             "2. Remove a product from your cart", 
                             "3. View your order", 
                             "4. Cancel your order", 
                             "5. Checkout"]

    def use(self):
        while True:
            print(f"Welcome to the cart menu {self.user.get_first_name()}")
            for option in self.menu_options:
                print(option)
            choice = input("Please enter a choice: ")
            
            if choice == "1":
                print("Please select a product from the catalogue:")
                suppliers_products = self.supplier.get_products()
                suppliers_products.print_products_with_numbers()
                option = int(input("Product: "))
                amount = int(input("Amount: "))
                selected_product = suppliers_products.get_product_from_index(option)
                if selected_product.has(amount):
                    order = Order(selected_product, amount)
                    self.orders.append(order)
                    print("Product added to cart.")
                else:
                    print("Not enough stock available!")
            
            elif choice == "2":
                if not self.orders:
                    print("Cart is empty!")
                else:
                    print("Which item would you like to remove?")
                    self.print_order_products_with_numbers()
                    item = int(input("Item: "))
                    if item <= len(self.orders):
                        self.orders.pop(item - 1)
                    else:
                        print("Invalid product!")
            
            elif choice == "3":
                print(self)
            
            elif choice == "4":
                print("Order cancelled!")
                break
            
            elif choice == "5":
                for order in self.orders:
                    order_product = order.get_product()
                    quantity = order.get_quantity()
                    profit = order_product.sell(quantity)
                    if isinstance(self.user, Customer):
                        self.supplier.add_profit(profit)
                    self.user.add_purchase(self)
                break
            
            else:
                print("Please enter a valid number, press 4 to cancel.")
    
    def __str__(self):
        order_string = f"Order from {self.supplier.get_region()}: \n"
        total_cost = 0
        for order in self.orders:
            order_product = order.get_product()
            quantity = order.get_quantity()
            order_string += f"{order_product.get_name()} ({quantity})\n]"
            total_cost += order_product.get_price() * quantity
        
        if isinstance(self.user, Manager):
            total_cost = 0
        
        order_string += f"Total Cost: {self.formatted(total_cost)}"
        return order_string
    
    def print_order_products_with_numbers(self):
        for i, order in enumerate(self.orders, start=1):
            order_product = order.get_product()
            quantity = order.get_quantity()
            print(f"{i}: {order_product.get_name()} ({quantity})")
    
    def formatted(self, price):
        return "{:,.2f}".format(price)


