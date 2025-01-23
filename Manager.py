from User import User
from Suppliers import Suppliers

class Manager(User):
    def __init__(self, first_name, last_name, username, password, suppliers):
        super().__init__(first_name, last_name, username, password)
        self.suppliers = Suppliers(suppliers)
        self.menu_options = ["1. View my details", 
                             "2. List all your suppliers", 
                             "3. Manage a particular supplier", 
                             "4. Logout"]

    def use(self, org):
        while True:
            print(f"Welcome to the manager menu {self.get_first_name()}.")
            for option in self.menu_options:
                print(option)
            choice = input("Please enter a choice: ")

            if choice == "1":
                print(f"{self.get_full_name()}, manager for: ")
                self.suppliers.print_supplier_regions()

            elif choice == "2":
                print("All suppliers:")
                print(self.suppliers)

            elif choice == "3":
                while True:
                    print("Which supplier would you like to manage?")
                    self.suppliers.print_supplier_regions_with_dot_numbers()
                    store = int(input("Supplier: "))
                    try:
                        supplier = self.suppliers.get_supplier_from_index(store)
                        supplier.manage(self)
                        break
                    except IndexError:
                        print("No such supplier!")

            elif choice == "4":
                break

            else:
                print("Please enter a valid number, press 4 to logout.")
    
    def get_suppliers(self):
        return self.suppliers
    
    def __str__(self):
        return ""


