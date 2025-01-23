from User import User

class Customer(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
        # Initialize the menu_options attribute here
        self.menu_options = [
            "1. View my details", 
            "2. Shop", 
            "3. View my order history", 
            "4. Logout"
        ]

    def use(self, org):
        while True:
            print(f"Welcome to the customer menu {self.get_first_name()}.")
            for option in self.menu_options:
                print(option)
            choice = input("Please enter a choice: ")

            if choice == "1":
                print(self.get_full_name())
            elif choice == "2":
                organisation_suppliers = org.get_suppliers()
                while True:
                    print("Where would you like to shop?")
                    organisation_suppliers.print_supplier_regions_with_colon_numbers()
                    option = int(input("Enter a choice: "))
                    try:
                        selected_supplier = organisation_suppliers.get_supplier_from_index(option)
                        selected_supplier.use(self)
                        break
                    except IndexError:
                        print("Invalid option entered!")
            elif choice == "3":
                if not self.purchases:
                    print("No purchase history!")
                else:
                    for cart in self.purchases:
                        print(cart)
            elif choice == "4":
                break
            else:
                print("Please enter a valid number, press 4 to logout.")


    
    def __str__(self):
        return ""


